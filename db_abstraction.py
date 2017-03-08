import sqlite3

class worker:
	"""docstring for worker"""
	def __init__(self, table, statement, params=tuple()):
		self.table = table
		self.statement = statement
		self.params = params


	def query(self):
		conn = sqlite3.connect(self.table)
		cursor = conn.cursor()
		result = cursor.execute(self.statement, self.params).fetchall()
		cursor.close()
		return result


	def insert(self):
		conn = sqlite3.connect(self.table)
		cursor = conn.cursor()
		cursor.execute(self.statement, self.params)
		conn.commit()
		cursor.close()
