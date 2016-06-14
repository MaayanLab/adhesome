#!/usr/local/bin/python3

import os
import pandas as pd
from distutils.dir_util import copy_tree
from staticjinja import make_site

data_root = 'data/'

filters={}
def register(func):
	filters[func.__name__] = func

@register
def to_dict(df):
	return df.to_dict(orient='split')

@register
def pd_select(df, attr, val):
	return df[df[attr] == val]

def components():
	return pd.read_csv(data_root+'nrm3769-s1.csv')

def interactions():
	return None

def base_context(template):
	return {
		'page': os.path.splitext(os.path.split(template.filename)[-1])[0],
		'components': components(),
		'interactions': interactions(),
	}

site = make_site(
	contexts=[('.*', base_context)],
	filters=filters,
	extensions=['jinja2.ext.with_'],
	outpath='build')
site.render()
copy_tree('static/', 'build/')
