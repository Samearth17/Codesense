import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

text = 'The brown bear walked in the woods, searching for a nut to snack on.'

tokens = word_tokenize(text)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

punct_tokens = [word for word in tokens if word not in punctuations]
stop_words = set(stopwords.words('english'))

cleaned_tokens = [word for word in punct_tokens if word not in stop_words]

stemmed_tokens = [stemmer.stem(word) for word in cleaned_tokens]

lemmatized_tokens = [lemmatizer.lemmatize(word) for word in stemmed_tokens]

print(lemmatized_tokens)