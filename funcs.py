'''
Function definitions, exposed in jinja2:

{{ urlize("test/me") }} => test_me
'''

import re
from itertools import count
from config import config

funcs={'config': config}
def register_func(func):
	''' Build a dict of functions for jinja templates '''
	funcs[func.__name__] = func
	return func

@register_func
def urlize(name):
	''' Prepare strings for urls or as variables '''
	return re.sub(r'[^\w]', '_', name.lower())

@register_func
def evaluate(template, **kwargs):
	''' Process a jinja template and take the result as valid python '''
	return eval(config.site.get_template(template).render(**dict(funcs, **kwargs)))

register_func(count)
