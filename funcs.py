import re
from math import log
from itertools import count
from config import config

funcs={}

def register_func(func):
	''' Build a dict of functions for jinja templates '''
	funcs[func.__name__] = func
	return func

@register_func
def urlize(name):
	''' Prepare strings for urls or as variables '''
	return re.sub(r'[^\w]', '_', name.lower())

@register_func
def get_cursor():
	return config.con.cursor()

register_func(count)
