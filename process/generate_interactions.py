#!/usr/local/bin/python3

import pandas as pd

data_root = '../data/'

# Load Adhesome
adhesome = pd.read_csv(data_root + 'components.csv')

# Load Old interactions
old_interactions = pd.read_csv(data_root + 'interactions.csv')

# Load edges
edges = [s.split(',') for s in map(str.strip, open(data_root + 'PPIN_low_content_edge_list.csv', 'r'))]

# Prepare new interactions
interactions = pd.concat([
	pd.DataFrame(columns=['Source','Target','Effect','Type of Interaction','PMID']),
	old_interactions[['Source', 'Target', 'Effect', 'Type of Interaction', 'PMID']]])

def get_component(c, attr='Official Symbol'):
	try:
		return adhesome[adhesome[attr] == c][0]
	except:
		return None

for edge in edges:
	components = list(filter(None, [get_component(c) for c in edge]))
	if len(components)!=2:
		continue
	s, t = components
	interactions.append({'Source': s, 'Target': t}, ignore_index=True, inplace=True)

interactions.to_csv(data_root + 'interactions_new.csv', index=False)
