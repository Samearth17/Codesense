from flask import Flask, render_template
from collections import Counter

app = Flask(__name__)

@app.route('/')
def word_count():
	# read text file
	file = open('document.txt', 'r') 
	text = file.read() 
	words = text.split()

	# count words in the file
	word_count = Counter(words)

	# extract the ten most frequent words
	most_common = word_count.most_common(10)

	return render_template('visualize.html', most_common=most_common)

if __name__ == '__main__':
    app.run(debug=True)