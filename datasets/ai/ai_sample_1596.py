import collections
import re

def find_most_common_words(text):
    # remove special characters
    clean_text = re.sub('[^a-zA-Z]+', ' ', text)
    
    # tokenize
    words = clean_text.split(' ')
    
    # get counts
    counts = collections.Counter(words)
    
    # get most common
    most_common = counts.most_common()
    
    # print most common words
    for word, count in most_common:
        print(word + ' : ' + str(count))