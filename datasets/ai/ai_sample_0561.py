import praw
import sqlite3

conn = sqlite3.connect('RedditScraper.db')
c = conn.cursor()

c.execute("""CREATE TABLE comments (
 comment_id text,
 comment_body text
)""") 

reddit = praw.Reddit(
 client_id='YOUR_CLIENT_ID',
 client_secret='YOUR_CLIENT_SECRET',
 user_agent='YOUR_USER_AGENT'
)

for comment in reddit.subreddit('all').stream.comments():
 c.execute("INSERT INTO comments VALUES (?, ?)",
 (comment.id, comment.body))
 conn.commit()

conn.close()