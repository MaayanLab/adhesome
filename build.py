#!/usr/local/bin/python3

import os
import sqlite3
from distutils.dir_util import copy_tree
from staticjinja import make_site

# Establish connection to database
con = sqlite3.connect('data/db.sqlite3')

# Utility functions
def try_ignore(stmt):
	try:
		exec(stmt)
	except:
		pass

def trim_(s):
	i = s.rfind('_')
	if i != -1:
		return s[:i]
	else:
		return s

# Jinja Filters
filters={}
def register_filter(func):
	filters[func.__name__] = func

@register_filter
def header(table):
	return [trim_(desc[0]) for desc in table.description]

@register_filter
def first(table):
	return next(iter(table))

# Jinja Functions
funcs={}
def register_func(func):
	funcs[func.__name__] = func

@register_func
def query(stmt, *kargs):
	return con.cursor().execute(stmt, kargs)

# Remove old build directory
try_ignore(r"os.rmdir('build/')")

# Create build directory tree
try_ignore(r"os.makedirs('build/associations/')")

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
for name, in funcs['query']('select `Name` from `datasets`'):
	uri = name.lower().replace(' ', '_')
	site.get_template('_association.html').stream(name=name, uri=uri, **funcs).dump('build/associations/%s.html' % (uri))
	for typ in ['viz', 'sim_row', 'sim_col']:
		site.get_template('_association_clustergram.html').stream(name=name, typ=typ, **funcs).dump('build/associations/%s_%s.html' % (uri, typ))
	print('Rendering %s' % (uri))
