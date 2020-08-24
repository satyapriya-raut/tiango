import sqlite3 as db

with db.connect("Tiango.sqlite") as con:
	cur = con.cursor()
	table = "User"
	query = 'SELECT * FROM {} WHERE id = ?'.format(table)
	rows = cur.execute(query,("satya",));
for row in rows:
	print(row)
print(query)
	
"""
cur.execute("SELECT * FROM PythonAttempted WHERE id = ?", ("satya",));
rows = cur.fetchone()
for row in rows:
	print(row)
"""
cur.execute("SELECT * FROM PythonScore ORDER BY Score DESC");
rows = cur.fetchall()
print(rows)
