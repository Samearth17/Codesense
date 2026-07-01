import nltk
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentences = sent_tokenize("The movie was so amazing!")

# Setup VADER sentiment intensity analyzer
analyzer = SentimentIntensityAnalyzer()

# Use VADER to get sentiment scores for each sentence
for sentence in sentences:
 scores = analyzer.polarity_scores(sentence)
 score = scores['compound']
 if score >= 0.1:
  sentiment = 'positive'
 elif score <= -0.1:
  sentiment = 'negative'
 else:
  sentiment = 'neutral'

 print(sentence + ': ' + sentiment)

# Output: The movie was so amazing!: positive