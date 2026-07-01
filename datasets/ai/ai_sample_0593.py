# import libraries
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from heapq import nlargest
 
# Define text summarization function
def summarize(text):
    # Tokenize text
    words = word_tokenize(text)
 
    # Calculate word frequencies
    word_frequencies = FreqDist(words)
    # Identify the most frequecny words
    most_frequent_words = nlargest(100, word_frequencies, key=word_frequencies.get)
 
    # Identify sentences
    sentences = sent_tokenize(text)
 
    # Calculate sentence score based on most frequent words
    sentence_scores = {} 
    for sentence in sentences:
        score = 0
        for word in word_tokenize(sentence.lower()):
            if word in most_frequent_words:
                score += 1
        sentence_scores[sentence] = score
 
    # Choose the highest score sentences from the list
    summarized_text = nlargest(7, sentence_scores, key=sentence_scores.get)
 
    return ' '.join(summarized_text)