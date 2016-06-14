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
def pd_to_table(df):
	return df.to_dict(orient='split')

@register
def pd_select(df, attr, val):
	return df[df[attr] == val]

@register
def pd_apply_format(df, attr, fmt):
	df[attr] = df[attr].apply(fmt.format)
	return df

def components():
	return pd.read_csv(data_root+'nrm3769-s1.csv')

def interactions():
	return None

def base_context(template):
	return {
		'components': components(),
		'interactions': interactions(),
	}

site = make_site(
	contexts=[('.*', base_context)],
	filters=filters,
	outpath='build')
site.render()
copy_tree('static/', 'build/')
