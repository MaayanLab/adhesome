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

@register
def trim_(data):
	i = data.rfind('_')
	return data[:i] if i!=-1 else data

def context(template):
	components = pd.read_csv(data_root+'components.csv', index_col=False)
	interactions = pd.read_csv(data_root+'interactions.csv', index_col=False)

	# Create interaction table

	# prepare columns
	interaction_components = components[['Official Symbol', 'Swiss-Prot ID', 'Functional Category', 'FA']]
	source_components = interaction_components.rename(columns={col: '%s_source' % (col) for col in components.columns})
	target_components = interaction_components.rename(columns={col: '%s_target' % (col) for col in components.columns})
	# merge components into interactions
	interactions_joined = pd.merge(
		pd.merge(interactions, source_components,
			left_on='Source', right_on='Official Symbol_source', how='inner'), target_components,
			left_on='Target', right_on='Official Symbol_target', how='inner', suffixes=('_','')).drop(
				['Official Symbol_source', 'Official Symbol_target'], axis=1)
	# rearrange columns
	source_cols = [col for col in interactions_joined.columns if col.endswith('_source')]
	target_cols = [col for col in interactions_joined.columns if col.endswith('_target')]
	cols 		= [col for col in interactions_joined.columns if col not in source_cols and col not in target_cols and col not in ['Source', 'Target']]
	interactions_joined = interactions_joined[['Source']+source_cols+['Target']+target_cols+cols]

	return {
		'components': components,
		'interactions': interactions_joined,
	}

site = make_site(
	contexts=[('.*', context)],
	filters=filters,
	outpath='build')
site.render()
copy_tree('static/', 'build/')
