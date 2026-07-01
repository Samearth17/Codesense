import sqlite3

# connect to the database
conn = sqlite3.connect('books.db')
c = conn.cursor()

# retrieve the data
c.execute('''SELECT title, author, genre, sales
FROM Books
WHERE genre='Fantasy'
ORDER BY sales DESC
LIMIT 10''')

# save the results
results = c.fetchall()

# generate the HTML code
html = '<table>'
html += '<tr><th>Title</th><th>Author</th><th>Genre</th><th>Sales</th></tr>'

for result in results:
 title = result[0]
 author = result[1]
 genre = result[2]
 sales = result[3]

 html += f'<tr><td>{title}</td><td>{author}</td><td>{genre}</td><td>{sales}</td></tr>'

html += '</table>'

# display the results
print(html)