#!/usr/local/bin/python3

import os
from distutils.dir_util import copy_tree
from staticjinja import make_site


filters={}
def register(func):
	filters[func.__name__] = func

def components():
	import pandas as pd
	df = pd.read_excel('nrm3769-s1.xlsx', header=[0], skiprows=[1, 150,])
	df['FA'] = ['Intrinsic Proteins' if n < 150 else 'Associated Protiens' for n, _ in df.iterrows()]
	return df.to_dict(orient='split')

def interactions():
	return None

def base_context(template):
	return {
		'page': os.path.splitext(os.path.split(template.filename)[-1])[0],
		'components': components(),
		'interactions': interactions(),
	}

site = make_site(contexts=[('.*', base_context)],
	filters=filters,
	extensions=['jinja2.ext.with_'],
	outpath='build')
site.render()
copy_tree('static/', 'build/')
