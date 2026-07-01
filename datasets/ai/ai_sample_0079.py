import re
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

def sentiment_analyzer(text):
    # Tokenize the text
    tokens = word_tokenize(text)

    # Create stemmer object
    stemmer = SnowballStemmer('english')

    # Stem each token
    stemmed_words = [stemmer.stem(word) for word in tokens]

    # Remove punctuation
    clean_words = [word for word in stemmed_words if re.match('[a-zA-Z-]+$', word)]

    # Remove stopwords
    meaningful_words = [word for word in clean_words if not word in stopwords.words('english')]

    # Create a SentimentIntensityAnalyzer object
    sid = SentimentIntensityAnalyzer()

    # Get the polarity score of the text
    polarity_score = sid.polarity_scores(' '.join(meaningful_words))

    return polarity_score