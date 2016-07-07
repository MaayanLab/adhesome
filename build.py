#!/usr/local/bin/python3

'''
Use staticjinja to build the website from templates directory.

We've extended this to handle building a number of pages from singular templates,
 this is done via an __init__ at the root of any directory with rules, for more
 see render_rules function.
'''

import os
import re
import shutil
import itertools
from staticjinja import make_site
from distutils.dir_util import copy_tree
from config import config
from filters import *
from funcs import *

# Source/Build directories
build = 'build'
templates = 'templates'

# Remove existing build directory or fail silently
try:
	shutil.rmtree(build)
except:
	pass

# Copy static files into build
copy_tree('static/', '%s/' % (build))

# Build standard pages
site = config.site = make_site(
	searchpath=templates,
	filters=filters,
	contexts=[(r'.*', funcs)],
	env_kwargs=dict(trim_blocks=True, lstrip_blocks=True),
	outpath=build)
site.render()

# Build rule based pages

def render(template, dump, **kwargs):
	''' Render custom page with jinja template engine '''
	print('Rendering %s...' % (dump))
	site.get_template(template).stream(**dict(funcs, **kwargs)).dump(os.path.join(build, dump))

def render_rules(rules):
	''' Given a rule dictionary, call render as specified
	Rule format:
		{
			"input_template", {
				"output_template", {
					"context", "variables",
				},
			},
			...
		}
	'''
	for in_template, rule in rules.items():
		for out_template, context in rule.items():
			render(in_template, out_template, **context)

render_rules( # Join all rules into a single dict and call render_rules
	dict(itertools.chain.from_iterable( # Flatten list ([[(a),(b)],[(c)]] -> [(a),(b),(c)])
		[evaluate(os.path.join(*os.path.split(r)[1:], '__init__')).items() # Evaluate the rule dict from the __init__ files in directories
		 for r, d, f in os.walk(templates) # Recursive traversal of templates directory
		 if not r.startswith('_') and '__init__' in f]))) # Only consider folders without preceeding _ and with __init__ file
