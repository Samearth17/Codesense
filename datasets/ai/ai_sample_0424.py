import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route('/save', methods=['POST'])
def save():
    # Extract request data
    title = request.json['title']
    content = request.json['content']

    # Connect to database
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()

    # Save blog post to database
    c.execute(
        'INSERT INTO blog_posts(title, content) VALUES(?, ?)',
        (title, content)
    )
    conn.commit()
    conn.close()

    return 'Blog post saved successfully!'

if __name__ == '__main__':
    app.run(debug=True)