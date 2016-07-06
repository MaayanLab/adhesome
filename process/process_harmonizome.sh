#!/bin/bash

rm -r harmonizome
mkdir -p harmonizome
cp harmonizomedownloader.py harmonizome
cd harmonizome

./harmonizomedownloader.py

for d in */; do
	cd "$d"
	gunzip -f *
	cd ..
done

cd ..
./process_matrix.py harmonizome/*/gene_attribute_matrix.txt
