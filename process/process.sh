#!/bin/bash

./harmonizomedownloader.py

for d in */; do
	cd "$d" && gunzip *
done

./process_matrix.py */gene_attribute_matrix.txt
./process_clustergrammer.py */gene_attribute_matrix.csv
