#!/bin/bash

./harmonizomedownloader.py

for d in */; do
	cd "$d"
	gunzip *
	cd ..
done

./process_matrix.py */gene_attribute_matrix.txt
