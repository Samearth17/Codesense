# Import necessary libraries
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# Read input data
with open('input.txt', 'r') as f:
 data = f.read()

# Lowercase
data = data.lower()

# Clean up punctuation
data = re.sub(r'[^\w\s]', ' ', data)

# Tokenize words
data = nltk.word_tokenize(data)

# Remove stopwords
data = [w for w in data if w not in stopwords.words('english')]

# Write cleaned data to file
with open('output.txt', 'w') as f:
 f.write(' '.join(data))