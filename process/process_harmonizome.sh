#!/bin/bash

# ./harmonizomedownloader.py

# for d in */; do
# 	cd "$d"
# 	gunzip -f *
# 	cd ..
# done

./process_matrix.py */gene_attribute_matrix.txt
