#!/usr/local/bin/python
# Note: python2 because clustergrammer is python2

import os
import sys
import json
import sqlite3
import pandas as pd

# Location of clustergrammer
sys.path.insert(0, '../clustergrammer/')
sys.path.insert(0, '..')

# Load database
con = sqlite3.connect('../data/db.sqlite3')
cur = con.cursor()
# Load adhesome
adhesome = [gene[0] for gene in cur.execute('select `Official Symbol` from `components`')]

for arg in sys.argv[1:]:
	name = os.path.split(arg)[0]

	try:
		# Load Gene Attribute Matrix
		gene_attribute_matrix = pd.read_table(arg, index_col=0, skiprows=[1,2])
		gene_attribute_matrix.index.rename('GeneSym', inplace=True)
		gene_attribute_matrix.drop([gene_attribute_matrix.columns[n] for n in range(2)], axis=1, inplace=True)

		# Select Genes in Adhesome
		gene_attribute_matrix = gene_attribute_matrix[gene_attribute_matrix.index.isin(adhesome)]

		# TODO: Category: Title (see clustergrammer.js/txt)

		# Create Clustergrammer Vector
		vector_json = {
			'title': name,
			'filter': 'N_row_sum',
			'columns': [{
				'col_name': str(col_name),
				'data': [{
					'val': float(val),
					'row_name': str(ind),
				} for ind, val in zip(col.index, col)]
			} for col_name, col in gene_attribute_matrix.to_dict(orient='series').iteritems()],
		}

		# Custergrammer
		from clustergrammer import Network
		net = Network()
		net.load_vect_post_to_net(vector_json)
		net.make_clust(dist_type='cos',views=['N_row_sum', 'N_row_var'], dendro=True,
					   sim_mat=True, filter_sim=0.1, calc_cat_pval=False)

		# Insert into database
		cur.execute('insert into `datasets` (`Name`, `viz`, `sim_row`, `sim_col`) values (?, ?, ?, ?)',
			(name,
			 net.export_net_json('viz', indent='no-indent'),
			 net.export_net_json('sim_row', indent='no-indent'),
			 net.export_net_json('sim_col', indent='no-indent')))
		con.commit()
	except Exception as e:
		print "Couldn't process %s (%s)" % (name, e)
		continue
	print "Processed %s" % (name)
con.close()
