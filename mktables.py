import sqlite3
import json
conn = sqlite3.connect("world.db")
cursor = conn.cursor()
cursor.execute('DROP TABLE world')
cursor.execute('''
	CREATE TABLE world(
	  name VARCHAR(100) PRIMARY KEY,
	  continent VARCHAR(100),
	  area INT,
	  population INT,
	  gdp float,
	  tld VARCHAR(5),
	  capital VARCHAR(100),
	  flag VARCHAR(100)
	)
	''')
w = json.load(open("worldl.json"))
for c in w:
	cursor.execute('''
		INSERT INTO world (name,continent,area,population,
		                   gdp,tld,capital,flag) VALUES
		            (?,?,?,?,?,?,?,?)
		''', (c['name'],c['continent'],c['area'],c['population'],
			  c['gdp'],c['tld'],c['capital'],c['flag']))
conn.commit()
