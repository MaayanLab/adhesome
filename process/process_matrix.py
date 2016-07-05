#!/usr/local/bin/python
# Note: python2 because clustergrammer is python2

import os
import sys
import json
import sqlite3
import pandas as pd
# Note: StringIO doesn't work for some reason
# from StringIO import StringIO

# Location of clustergrammer
sys.path.insert(0, '../clustergrammer/')
sys.path.insert(0, '..')

# Load database
con = sqlite3.connect('../data/db.sqlite3')
cur = con.cursor()
# Load adhesome
adhesome = [gene for gene, in cur.execute('select `Official Symbol` from `components`')]

for arg in sys.argv[1:]:
	name = os.path.split(arg)[0]

	try:
		# Load Gene Attribute Matrix
		gene_attribute_matrix = pd.read_table(arg, header=[0,1,2], index_col=[0,1,2])
		# Drop un-needed indexes/headers
		gene_attribute_matrix.index = gene_attribute_matrix.index.droplevel([1,2])
		gene_attribute_matrix.columns = gene_attribute_matrix.columns.droplevel([1,2])
		# gene_attribute_matrix.columns.name='\t' # Rename header column from #
		# Select Genes in Adhesome
		gene_attribute_matrix = gene_attribute_matrix[gene_attribute_matrix.index.get_level_values(0).isin(adhesome)]
		# Format index/headers for clustergrammer
		gene_attribute_matrix.index = gene_attribute_matrix.index.map(lambda s: 'Gene: %s' % (s))
		gene_attribute_matrix.columns = gene_attribute_matrix.columns.map(lambda s: 'Cell Line: %s' % (s))
		# Write to file
		# fp = StringIO()
		# gene_attribute_matrix.to_csv(fp, sep='\t')
		gene_attribute_matrix.to_csv('tmp.txt', sep='\t')

		# Custergrammer
		from clustergrammer import Network
		net = Network()
		# net.load_tsv_to_net(fp, name) # StringIO
		net.load_file('tmp.txt')
		net.swap_nan_for_zero()
		# Generate
		net.make_clust(dist_type='cos',views=['N_row_sum', 'N_row_var'], dendro=True,
					   sim_mat=True, filter_sim=0.1, calc_cat_pval=False)

		# Insert into database
		cur.execute('insert into `datasets` (`Name`, `prot_att`, `att_att`, `prot_prot`) values (?, ?, ?, ?)',
			(name,
			 net.export_net_json('viz', indent='no-indent'),
			 net.export_net_json('sim_col', indent='no-indent'),
			 net.export_net_json('sim_row', indent='no-indent')))
		con.commit()
	except Exception as e:
		print "Couldn't process %s (%s)" % (name, e)
		continue
	print "Processed %s" % (name)
con.close()
