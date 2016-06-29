import json
from collections import OrderedDict
from jinja2 import Template
from config import config
from funcs import funcs, urlize

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
	new_data = []
	header_row = list(map(urlize, table['header']))
	for row in table['data']:
		row_dict = OrderedDict(zip(header_row, row))
		for k, sub in json.loads(subst).items():
			row_dict[k] = Template(sub.replace('[', '{').replace(']', '}')).render(**dict(row_dict, **funcs))
		new_data.append(row_dict.values())
	return dict(table, data=new_data)

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
def typ_lookup(typ):
	return config.typs.get(typ)

register_filter(next)
