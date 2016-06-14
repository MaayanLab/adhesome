#!/usr/local/bin/python3

import pandas as pd
import requests
import json

data_root = '../data/'

# Load Adhesome
adhesome = pd.read_csv(data_root + 'nrm3769-s1.csv')

# Load Gene Attribute Matrix (TODO: read this matrix from harmonizome)
gene_attribute_matrix = pd.read_table(data_root + 'gene_attribute_matrix_standardized.txt', index_col=0, skiprows=[1,2])
gene_attribute_matrix.index.rename('GeneSym', inplace=True)
gene_attribute_matrix.drop(['#.1', 'CellLine'], axis=1, inplace=True)

# Select Genes in Adhesome
gene_attribute_matrix = gene_attribute_matrix[gene_attribute_matrix.index.isin(adhesome['Official Symbol'])]
gene_attribute_matrix.to_csv('adhesome_gene_attribute_table.csv')

# Create Clustergrammer Vector
vector_json = {
	'title': 'Adhesome',
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

# Upload to Clustergrammer
upload_url = 'http://amp.pharm.mssm.edu/clustergrammer/vector_upload/'
r = requests.post(upload_url, json.dumps(vector_json))
response = json.loads(r.text)
print(response)
