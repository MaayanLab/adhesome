#!/usr/local/bin/python3

import os
import sqlite3
from distutils.dir_util import copy_tree
from staticjinja import make_site

con = sqlite3.connect('data/db.sqlite3')

funcs={}
def register_func(func):
	funcs[func.__name__] = func

filters={}
def register_filter(func):
	filters[func.__name__] = func

@register_filter
def header(table):
	return [desc[0] for desc in table.description]

@register_func
def query(stmt, *kargs):
	return con.cursor().execute(stmt, kargs)

def associations(env, template, **kwargs):
	env.get_template('_association.html').stream(**kwargs).dump(template)

site = make_site(
	searchpath='templates/',
	filters=filters,
	contexts=[('.*', funcs)],
	outpath='build')

# TODO:
# for ID in funcs['query']('select `ID` from `datasets`'):
# 	site.render_template('associations/%d.html' % (ID), dict(ID=ID), '_association.html')

site.render()

copy_tree('static/', 'build/')
