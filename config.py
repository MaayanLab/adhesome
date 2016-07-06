'''
Provides a singleton accessible throughout the project and in the templates for globals.
'''

import sqlite3

class Config:
	''' Borg class with globals '''
	__shared_state = None

	def __init__(self):
		if Config.__shared_state is None:
			self.typs = {
				"prot_att": "Protein-Attribute Table",
				"prot_prot": "Protein-Protein Similarity",
				"att_att": "Attribute-Attribute Similarity",
			}
			self.con = sqlite3.connect('data/db.sqlite3')
			self.cur = self.con.cursor()
			self.base = ''
		else:
			self.__dict__ = self.__shared_state

# Obtain [shared] instance, expose via import
config = Config()
