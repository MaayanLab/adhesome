'''
Use staticjinja to build the website from templates directory.

We've extended this to handle building a number of pages from singular templates,
 this is done via an __init__ at the root of any directory with rules, for more
 see render_rules function.
'''

import os
import re
import shutil
from staticjinja import make_site
from distutils.dir_util import copy_tree
from config import config
from filters import *
from funcs import *

# Remove existing build directory or fail silently
try:
	shutil.rmtree(config.build)
except:
	pass

# Copy static files into build
copy_tree('static/', '%s/' % (config.build))

# Build standard pages
site = config.site = make_site(
	searchpath=config.templates,
	filters=filters,
	contexts=[(r'.*', funcs)],
	env_kwargs=dict(trim_blocks=True, lstrip_blocks=True),
	outpath=config.build)
site.render()

# Build rule based pages

def render(template, dump, **kwargs):
	''' Render custom page with jinja template engine '''
	print('Rendering %s...' % (dump))
	site.get_template(template).stream(**dict(funcs, **kwargs)).dump(os.path.join(config.build, dump))

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

rules = {}
for r, d, f in os.walk(config.templates):
	if not r.startswith('_') and '__init__' in f:
		p = r.split(os.path.sep)[1:]
		# Create directory in build
		try:
			os.makedirs(os.path.join(config.build, *p))
		except:
			pass
		# Evaluate the rule dict from the __init__ files in directories
		rules.update(evaluate(os.path.join(*p, '__init__')))

render_rules(rules)
