# Importing the essential library 
import nltk
 
# Defining a function to tokenize a sentence
def tokenize(text):
    tokens = nltk.word_tokenize(text)
    tok_words = [tok for tok in tokens if tok.isalpha()]
    tok_punct = [tok for tok in tokens if not tok.isalpha()]
    return tok_words, tok_punct
 
if __name__ == '__main__':
    text = "This is a sample sentence."
    words, puncts = tokenize(text)
    print("Words:", words)
    print("Punctuations:", puncts)