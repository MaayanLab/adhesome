#!/usr/local/bin/python3

'''
Given the .xgmml files downloaded from BioGrid, this script converts the databases into .csv files
'''

import xml.etree.cElementTree as xml
import pandas as pd

e = xml.ElementTree(file='query---20062016_0233.xgmml')
r = e.getroot()

df = pd.DataFrame()
for node in r.iterfind('{http://www.cs.rpi.edu/XGMML}node'):
	df=df.append(dict({
		att.get('name'): att.get('value')
		for att in node.iterfind('{http://www.cs.rpi.edu/XGMML}att')},
		**dict(node.items())), ignore_index=True)
df.to_csv('node.csv')

df = pd.DataFrame()
for edge in r.iterfind('{http://www.cs.rpi.edu/XGMML}edge'):
	df=df.append(dict({
		att.get('name'): att.get('value')
		for att in node.iterfind('{http://www.cs.rpi.edu/XGMML}att')},
		**dict(node.items())), ignore_index=True)
df.to_csv('edges.csv')
