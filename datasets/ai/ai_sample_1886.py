import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Create the sentiment analyzer object
sentiment_analyzer = SentimentIntensityAnalyzer()

# Read the text document
text = open('example.txt', 'r').read()

# Get the sentiment scores
sentiment_scores = sentiment_analyzer.polarity_scores(text)

# Print the sentiment
for key in sentiment_scores:
 print('{0}: {1}, '.format(key, sentiment_scores[key]), end='')

print('\nThe sentiment of the text is: ', end='')

if sentiment_scores['compound'] >= 0.05:
 print('Positive')
elif sentiment_scores['compound'] <= - 0.05:
 print('Negative')
else:
 print('Neutral')