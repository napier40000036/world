#Create sqlite database from json
import sqlite3
import json
conn = sqlite3.connect("world.db")
c = conn.cursor()
#c.execute("DROP TABLE world")
c.execute('''
	CREATE TABLE world(
	  name VARCHAR(100) PRIMARY KEY,
	  continent VARCHAR(20),
	  area INT,
	  population INT,
	  GDP float,
	  capital VARCHAR(100),
	  tld VARCHAR(5),
	  flag VARCHAR(100)
	)
	''')
w = json.load(open("worldl.json"))
for ct in w:
	print ct['name']
	insert = "INSERT INTO world(name,continent,area,population,gdp,tld,capital,flag) VALUES (?,?,?,?,?,?,?,?)"
	c.execute(insert,(ct['name'],ct['continent'],ct['area'],ct['population'],ct['gdp'],ct['tld'],ct['capital'],ct['flag']))
conn.commit()

