'''
Function definitions, exposed in jinja2:

{{ urlize("test/me") }} => test_me
'''

from itertools import count
from config import config

funcs={'config': config}
def register_func(func):
	''' Build a dict of functions for jinja templates '''
	funcs[func.__name__] = func
	return func

@register_func
def evaluate(template, **kwargs):
	''' Process a jinja template and take the result as valid python '''
	return eval(config.site.get_template(template).render(**dict(funcs, **kwargs)))

register_func(count)
