#!/usr/local/bin/python3

import os
import sys
import json
import sqlite3
import pandas as pd

# Load database
con = sqlite3.connect('../data/db.sqlite3')
cur = con.cursor()
# Load adhesome
adhesome = [gene[0] for gene in cur.execute('select `Official Symbol` from `components`')]

for arg in sys.argv[1:]:
	name = os.path.split(arg)[0]

	# Load Gene Attribute Matrix
	gene_attribute_matrix = pd.read_table(arg, index_col=0, skiprows=[1,2])
	gene_attribute_matrix.index.rename('GeneSym', inplace=True)
	gene_attribute_matrix.drop([gene_attribute_matrix.columns[n] for n in range(2)], axis=1, inplace=True)

	# Select Genes in Adhesome
	gene_attribute_matrix = gene_attribute_matrix[gene_attribute_matrix.index.isin(adhesome)]

	# Create Clustergrammer Vector
	vector_json = {
		'title': name,
		'filter': 'N_row_sum',
		'columns': [{
			'cat': 'CellLine',
			'col_name': str(col_name),
			'data': [{
				'val': float(val),
				'row_name': str(ind),
			} for ind, val in zip(col.index, col)]
		} for col_name, col in gene_attribute_matrix.to_dict(orient='series').items()],
	}

	# Insert into database
	cur.execute('insert into `datasets` (`Name`, `Clustergrammer`) values (?, ?)', (name, json.dumps(vector_json)))

con.commit()
con.close()
