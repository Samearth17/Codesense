def classify_books(books):
    # Use a dictionary to store book title and corresponding genres
    titles_and_genres = {
        'The Catcher in the Rye': 'Fiction',
        'To Kill a Mockingbird': 'Novel',
        'Pride and Prejudice': 'Romance',
        'The Hunger Games': 'Young Adult Fiction'
    }

    result = [] 
    for book in books:
        title = book[0]
        author = book[1]
        genre = titles_and_genres[title]
        result.append({'title': title, 'author': author, 'genre': genre})
    return result 

books = [('The Catcher in the Rye', 'J.D. Salinger'), 
         ('To Kill a Mockingbird', 'Harper Lee'),
         ('Pride and Prejudice', 'Jane Austen'),
         ('The Hunger Games', 'Suzanne Collins')]
print(classify_books(books))