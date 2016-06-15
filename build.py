#!/usr/local/bin/python3

import os
import sqlite3
from distutils.dir_util import copy_tree
from staticjinja import make_site

data_root = 'data/'

filters={}
def register(func):
	filters[func.__name__] = func

@register
def header(table):
	return [desc[0] for desc in table.description]

def context(template):
	con = sqlite3.connect(data_root+'db.sqlite3')

	return {
		'components': con.cursor().execute('select * from components_out'),
		'interactions': con.cursor().execute('select * from interactions_out'),
	}

site = make_site(
	contexts=[('.*', context)],
	filters=filters,
	outpath='build')
site.render()
copy_tree('static/', 'build/')
