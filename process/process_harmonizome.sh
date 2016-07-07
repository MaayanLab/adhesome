#!/bin/bash

# Download datasets if not already done
if [ ! -d "harmonizome" ]; then
	mkdir harmonizome
	cp harmonizomedownloader.py harmonizome
	cd harmonizome
	./harmonizomedownloader.py
	for d in */; do
		cd "$d"
		gunzip -f *
		cd ..
	done
	cd ..
fi

# Process files not in the database
python3 - << END
import os, sys, sqlite3, subprocess
con = sqlite3.connect('../data/db.sqlite3')
existing = [name for name, in con.cursor().execute('select Name from datasets')]
files = [os.path.join(r, 'gene_attribute_matrix.txt')
		 for r, d, _ in os.walk('harmonizome')
		 if not d and os.path.split(r)[-1] not in existing]
subprocess.call(['./process_matrix.py', *files])
END
