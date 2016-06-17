#!/usr/local/bin/python3

import os
import sqlite3
import json
from itertools import count
from collections import OrderedDict
from distutils.dir_util import copy_tree
from staticjinja import make_site
from jinja2 import Template

# Establish connection to database
con = sqlite3.connect('data/db.sqlite3')

def try_ignore(stmt):
	''' For statements we expect to throw exceptions and move on '''
	try:
		exec(stmt)
	except:
		pass

# Jinja Functions
funcs={}
def register_func(func):
	''' Build a dict of functions for jinja templates '''
	funcs[func.__name__] = func
	return func

@register_func
def urlize(name):
	''' Prepare strings for urls or as variables '''
	return name.replace(' ', '_').lower()

@register_func
def query(stmt, *kargs):
	''' Query the database retreiving both the header and all the rows '''
	table = con.cursor().execute(stmt, kargs)
	return {
		'header': [desc[0] for desc in table.description],
		'data': table.fetchall()
	}

# Jinja Filters
filters={}
def register_filter(func):
	''' Build a dict of filters for jinja templates '''
	filters[func.__name__] = func
	return func

@register_filter
def trim_(s):
	''' Remove everything after the last _ '''
	i = s.rfind('_')
	if i != -1:
		return s[:i]
	else:
		return s

@register_filter
def apply(table, subst):
	''' This filter lets us substitute column entries in our tables via template substitution 
	 just use [ ] instead of { } so it doesn't conflict with the existing template. '''
	new_data = []
	for row in table['data']:
		row_dict = OrderedDict(zip(map(urlize, table['header']), row))
		for k, sub in json.loads(subst).items():
			row_dict[k] = Template(sub.replace('[', '{').replace(']', '}')).render(**dict(row_dict, **funcs))
		new_data.append(row_dict.values())
	table['data'] = new_data
	return table

register_func(count)
register_filter(next)

# Remove old build directory
try_ignore(r"os.rmdir('build/')")

# Create build directory tree
try_ignore(r"os.makedirs('build/associations/')")
try_ignore(r"os.makedirs('build/components/')")

# Copy static files to build
copy_tree('static/', 'build/')

# Build static pages
site = make_site(
	searchpath='templates/',
	filters=filters,
	contexts=[('.*', funcs)],
	outpath='build')
site.render()

# Build subpages from database
for name, in query('select `Name` from `datasets`')['data']:
	uri = name.lower().replace(' ', '_')
	site.get_template('_association.html').stream(name=name, uri=uri, **funcs).dump('build/associations/%s.html' % (uri))
	for typ in ['viz', 'sim_row', 'sim_col']:
		site.get_template('_association_clustergram.html').stream(name=name, typ=typ, **funcs).dump('build/associations/%s_%s.html' % (uri, typ))
	print('Rendering %s' % (uri))

site.get_template('_component_all.html').stream(**funcs).dump('build/components/all.html')
print('Rendering all components')

for name, in query('select `Official Symbol` from `components`')['data']:
	site.get_template('_component.html').stream(name=name, **funcs).dump('build/components/%s.html' % (name))
	print('Rendering %s' % (name))
