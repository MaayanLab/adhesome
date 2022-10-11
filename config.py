'''
Provides a singleton accessible throughout the project and in the templates for globals.
'''

import sqlite3
from collections import OrderedDict

class Config:
	''' Borg class with globals '''
	__shared_state = None

	def __init__(self):
		if Config.__shared_state is None:
			self.typs = OrderedDict((
				("prot_prot", "Protein-Protein Similarity"),
				("prot_att", "Protein-Attribute Table"),
				("att_att", "Attribute-Attribute Similarity"),
			))
			self.con = sqlite3.connect('data/db.sqlite3')
			self.cur = self.con.cursor()
			self.base = ''
			self.build = 'build'
			self.templates = 'templates'
			self.jupyter_nbconvert = 'jupyter-nbconvert'
			self.curl = "curl"
		else:
			self.__dict__ = self.__shared_state

# Obtain [shared] instance, expose via import
config = Config()
