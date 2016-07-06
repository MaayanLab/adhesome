'''
Filter definitions, exposed in jinja2:

{{ "test_me"|trim_ }} => test
'''

import json
from collections import OrderedDict
from jinja2 import Template
from config import config
from funcs import funcs, urlize
from copy import copy

filters={}
def register_filter(func):
	''' Build a dict of filters for jinja templates '''
	filters[func.__name__] = func
	return func

@register_filter
def trim_(s):
	''' Remove everything after the last _ '''
	i = s.rfind('_')
	if i != -1:
		return s[:i]
	else:
		return s

@register_filter
def query_exec(cur, stmt, *kargs):
	''' Query the database '''
	return cur.execute(stmt, kargs)

@register_filter
def query(cur, stmt, *kargs):
	''' Query the database retreiving both the header and all the rows '''
	table = query_exec(cur, stmt, *kargs)
	return {
		'header': [desc[0] for desc in table.description],
		'data': table.fetchall()
	}

@register_filter
def apply(table, subst):
	''' This filter lets us substitute column entries in our tables via template substitution
	 just use [ ] instead of { } so it doesn't conflict with the existing template. '''
	subst = json.loads(subst)

	header = table['header']
	new_header = [h for h in header
				  if subst.get(urlize(h), None) is not ""]

	header_row = list(map(urlize, header))
	new_header_row = list(map(urlize, new_header))

	# Substitute Data
	new_data = []
	for row in table['data']:
		row_dict = OrderedDict(zip(header_row, row))
		context = dict(row_dict, **funcs)
		for k, sub in subst.items():
			row_dict[k] = Template(sub.replace('[', '{').replace(']', '}')).render(**context)
		new_data.append([v for k,v in row_dict.items()
						   if k in new_header_row])

	return {
		'header': new_header,
		'data': new_data
	}

@register_filter
def unique_edges(array):
	''' This filter removes duplicated edges and assumes:
	 - [0] == source, [1] == target, [2:] == the rest are concatable '''
	pairs = {}
	for entry in array:
		key = tuple(sorted(entry[:2]))
		if key[0] != key[1]:
			if pairs.get(key):
				for a, b in zip(pairs[key], entry[2:]):
					a += b
			else:
				pairs[key] = entry[2:]
	return [k+tuple(v) for k,v in pairs.items()]

@register_filter
def jsonify(data):
	''' Python -> JSON '''
	return json.dumps(data)

@register_filter
def one_tuple(data):
	''' Helper function for one_tuples as jinja2 doesn't support it '''
	return (a for a, in data)

register_filter(next)
