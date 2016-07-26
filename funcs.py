'''
Function definitions, exposed in jinja2:

{{ urlize("test/me") }} => test_me
'''

import os
from itertools import count
from config import config
from subprocess import Popen, PIPE

funcs={'config': config}
def register_func(func):
	''' Build a dict of functions for jinja templates '''
	funcs[func.__name__] = func
	return func

@register_func
def include(template, **kwargs):
	''' Custom include which supports passing named arguments '''
	return config.site.get_template(template).render(**dict(funcs, **kwargs))

@register_func
def evaluate(template, **kwargs):
	''' Process a jinja template and take the result as valid python '''
	return eval(include(template, **kwargs))

@register_func
def build_notebook(url):
	return Popen([config.jupyter_nbconvert, '--to', 'html' ,'--template', 'basic', '--stdin', '--stdout'],
				stdin=Popen([config.curl, url],
							stdout=PIPE).stdout,
				stdout=PIPE).communicate()[0].decode()

register_func(count)
