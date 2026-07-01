import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

text = 'The food was delicious but the service was slow.'
sid = SentimentIntensityAnalyzer()
ss = sid.polarity_scores(text)

if ss['compound'] >= 0.5:
 print('Positive sentiment')
elif ss['compound'] <= -0.5:
 print('Negative sentiment')
else:
 print('Neutral sentiment')

Output:
Negative sentiment