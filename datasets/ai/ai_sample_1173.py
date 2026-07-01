import nltk
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.collocations import *

def get_hashtag(sentence):
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    words = tokenizer.tokenize(sentence)

    bigram_measures = nltk.collocations.BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(words)

    #ignore punctuation and stopwords
    stop_words = stopwords.words('english')
    finder.apply_word_filter(lambda x: x in stop_words)
    finder.apply_word_filter(lambda x: x.isalpha() == False)

    hashtag = finder.nbest(bigram_measures.pmi,1)
    return "#" + hashtag[0][0] + hashtag[0][1]

sentence = "We are going on a picnic"
result = get_hashtag(sentence)
print(result) # Output = #GoingPicnic