import sqlite3

#connect to the database
conn = sqlite3.connect('example.db')
c = conn.cursor()

#program loop 
while True:
	#input search query
	search_term = input('Enter search query: ')
	#execute query
	c.execute("SELECT * from records WHERE search_term LIKE ?", ('%'+search_term+'%',))
	#fetch and print results
	results = c.fetchall()
	print('Results: ')
	for result in results:
		print(result)