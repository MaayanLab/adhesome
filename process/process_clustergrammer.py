#!/usr/local/bin/python3

import sys
import pandas as pd
import requests
import json

for arg in sys.argv[1:]:
	# Load gene attribute matrix
	gene_attribute_matrix = pd.read_csv('gene_attribute_table.csv')

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

	print(response['link'])
