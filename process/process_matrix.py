#!/usr/local/bin/python3

import os
import sys
import pandas as pd

data_root = '../data/'

# Load Adhesome
adhesome = pd.read_csv(data_root + 'nrm3769-s1.csv')

for arg in sys.argv[1:]:
	# Load Gene Attribute Matrix
	gene_attribute_matrix = pd.read_table(arg, index_col=0, skiprows=[1,2])
	gene_attribute_matrix.index.rename('GeneSym', inplace=True)
	gene_attribute_matrix.drop([gene_attribute_matrix.columns[n] for n in range(2)], axis=1, inplace=True)

	# Select Genes in Adhesome
	gene_attribute_matrix = gene_attribute_matrix[gene_attribute_matrix.index.isin(adhesome['Official Symbol'])]
	gene_attribute_matrix.to_csv('%s.csv' % (os.path.splitext(arg)[0]))
