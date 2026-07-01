import sqlite3
import tkinter

# create the Tkinter window
root = tkinter.Tk()

# set up the sqlite connection
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

# create the table
cursor.execute("""CREATE TABLE IF NOT EXISTS movies (
 title TEXT,
 genre TEXT
)""")

# create labels for the search boxes
search_title = tkinter.Label(root, text="Title:")
search_genre = tkinter.Label(root, text="Genre:")

# create search boxes
title_box = tkinter.Entry(root)
genre_box = tkinter.Entry(root)

# create a button to submit the search
submit_button = tkinter.Button(root,
                       text="Submit",
                       command=search_movies)

#function that handles the whole search
def search_movies():
    title = title_box.get()
    genre = genre_box.get()

    # build the sql query
    query = """SELECT * FROM movies WHERE"""
    if title != '':
        query+=f""" title="{title}" AND"""
    if genre != '':
        query+=f""" genre="{genre}"""
    query = f"""{query} ORDER BY title asc;"""

    # execute the query
    cursor.execute(query)
 §§ 1131
    rows = cursor.fetchall()

    #render the data in the table
    for row in rows:
        row_text = f""" Title: {row[0]}, Genre: {row[1]}"""
        row_label = tkinter.Label(root, text=row_text)
        row_label.pack()

#pack the widgets
search_title.pack()
title_box.pack()

search_genre.pack()
genre_box.pack()

submit_button.pack()

root.mainloop()