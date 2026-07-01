class TextProcessor:
    def __init__(self):
        pass
    
    def remove_punctuation(self, text):
        # remove punctuation
        no_punct = "".join([c for c in text if c not in string.punctuation])
        return no_punct
 
    def remove_stopwords(self, text):
        # remove stopwords
        no_stopwords = [w for w in text if w not in stopwords.words('english')]
        return no_stopwords
    
    def lemmatize_words(self, text):
        # lemmatize words
        lemmatizer = WordNetLemmatizer()
        lemmatized = [lemmatizer.lemmatize(word) for word in text]
        return lemmatized