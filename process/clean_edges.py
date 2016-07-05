#!/usr/local/bin/python3

'''
With edges sometimes defined one way and not the other (Source -> Target vs Target -> Source),
 and with multiple duplicate edges with and without unique PMIDs, the data was somewhat messy.

For that this script was devized which does the following:
 - Load edges from database
 - Populate table with Source, Target & Target, Source
 - Take out string appended PMIDs for each Source, Target group
 - Remove all duplicate edges, PMID pairs
 - Write back to the database
'''

import sqlite3
import pandas as pd
import itertools as it


def swap(df, a, b):
	''' Swap two DataFrame columns' values '''
	df.loc[:,[a, b]]=df.loc[:,[b, a]].values
	return df

# Get from database
con = sqlite3.connect('../data/db.sqlite3')
cur = con.cursor()
q  = cur.execute('select * from `edges`')
cols = [desc[0] for desc in q.description]
df = pd.DataFrame(list(q), columns=cols)

# Append all the edges reversed to the list
df = pd.concat([df, swap(df.copy(), 'Source', 'Target')]).reset_index(drop=True)

# Separate out all PMIDs
new_df = pd.DataFrame(
	[(st[0], st[1], df.ix[i]['Effect'], df.ix[i]['Type'], pmid, df.ix[i]['data_source'])
	for st, ids in df.groupby(['Source', 'Target']).groups.items()
	for i in ids
	for pmid in df.ix[i]['PMID'].split(' ')], columns=cols)

# Remove all duplicates
new_df = new_df.sort_values('data_source').drop_duplicates(subset=['Source', 'Target', 'PMID'])
# note: adhesome.org will get sorted towards the top, we want to preserve adhesome.org over any of the others
#  because our edges don't have any unique type and binding information

# Remove all feedbacks
new_df = new_df[new_df['Source']!=new_df['Target']]

# Write back to database
cur.execute('delete from `edges`')
new_df.apply(lambda d: cur.execute('insert into `edges` values (%s)' % (','.join('?'*len(cols))), d), axis=1)
con.commit()
