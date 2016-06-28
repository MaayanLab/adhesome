#!/usr/local/bin/python3

import os
import re
import shutil
from distutils.dir_util import copy_tree
from staticjinja import make_site
from filters import *
from funcs import *
from config import config

def try_ignore(stmt):
	''' For statements we expect to throw exceptions and move on '''
	try:
		exec(stmt)
	except:
		pass

# Re-create build directory
try_ignore(r"shutil.rmdir('build/')")
try_ignore(r"os.makedirs('build/associations/')")
try_ignore(r"os.makedirs('build/components/')")
copy_tree('static/', 'build/')

# Build static pages
site = make_site(
	searchpath='templates/',
	filters=filters,
	contexts=[('.*', funcs)],
	env_kwargs=dict(trim_blocks=True, lstrip_blocks=True),
	outpath='build')
site.render()

def render(template, dump, **kwargs):
	''' Render custom page with jinja engine '''
	print('Rendering %s...' % (dump))
	site.get_template(template).stream(**dict(funcs, **kwargs)).dump(dump)

# Build subpages from database
cur = get_cursor()
for name, in query(cur, 'select `Name` from `datasets`')['data']:
	uri = urlize(name)
	for typ, typ_name in config.typs.items():
		render('_association.html', 'build/associations/%s_%s.html' % (uri, typ),
			name=name, typ=typ, uri=uri)

# Build component subpages
render('_component_all.html', 'build/components/all.html')
for name, in query(cur, 'select `Official Symbol` from `components`')['data']:
	render('_component.html', 'build/components/%s.html' % (name), name=name)
