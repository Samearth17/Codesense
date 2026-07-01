import nltk
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def classify_tweet(text):
 tokenized_text = nltk.word_tokenize(text)
 tag = nltk.pos_tag(tokenized_text)
 lemmatizer = nltk.WordNetLemmatizer()
 lemmas = [lemmatizer.lemmatize(word) for word, tag in tag]

 sentiment_analyzer = SentimentIntensityAnalyzer()
 sentiment = sentiment_analyzer.polarity_scores(' '.join(lemmas))

if sentiment['compound'] < 0:
 print('Negative')
elif sentiment['compound'] > 0:
 print('Positive')
else:
 print('Neutral')

classify_tweet("I am really enjoying this course!")
# Output: Positive