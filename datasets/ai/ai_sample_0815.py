import nltk
import pandas as pd
import numpy as np

# Input text
text = "This is a sample text for Keyword extraction."

# Tokenize words
words = nltk.word_tokenize(text)

# Initialize corpus
corpus = []

# Convert tokens to lowercase
for word in words:
     corpus.append([word.lower()])

# Get unigrams
wordsFreq = pd.DataFrame(corpus, columns=['Word'])

# Calculate document frequency
df = wordsFreq.groupby('Word').size().reset_index(name='Doc Frequency')

# Calculate term frequency
tf = wordsFreq['Word'].value_counts().reset_index(name='Term Frequency')

# Merge both frequencies for computing TF - IDF
tfidf = pd.merge(df, tf, on='Word', how='inner')

# Calculate Inverse Document Frequency
tfidf['Inverse Document Frequency'] = np.log(len(text)/(tfidf['Doc Frequency'] + 1))

# Calculate TF - IDF
tfidf['TF - IDF'] = tfidf['Term Frequency'] * tfidf['Inverse Document Frequency']

# Sort words by TF - IDF in descending order
tfidf.sort_values('TF - IDF', ascending=False, inplace=True)

# Print the most important words
print(tfidf[:5]['Word'])
# Output:
# 0      sample
# 1   keyword
# 2    extract
# 3        for
# 4        this