import string
import nltk 
nltk.download('punkt')

# remove punctuation and capitalization 
def remove_punctuation_and_make_lowercase(data):
  table = str.maketrans({key: None for key in string.punctuation})
  data_without_punctuation = data.translate(table).lower()
  return data_without_punctuation

data = "The product was good, but customer service was slow"

data_without_punctuation = remove_punctuation_and_make_lowercase(data)
print(data_without_punctuation)

# tokenize
data_tokenized = nltk.word_tokenize(data_without_punctuation)
print(data_tokenized)