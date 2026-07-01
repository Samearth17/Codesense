import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentences = ["I am happy.", "I am not happy.", "This is great!"]

analyzer = SentimentIntensityAnalyzer()

for sentence in sentences:
    scores = analyzer.polarity_scores(sentence)
    print(f"{sentence} : {scores}")

# Output: 
# I am happy. : {'neg': 0.0, 'neu': 0.357, 'pos': 0.643, 'compound': 0.6249}
# I am not happy. : {'neg': 0.504, 'neu': 0.496, 'pos': 0.0, 'compound': -0.5859}
# This is great! : {'neg': 0.0, 'neu': 0.312, 'pos': 0.688, 'compound': 0.6249}