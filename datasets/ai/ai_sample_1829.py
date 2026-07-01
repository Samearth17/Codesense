import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

# Function to tokenize text into words
def tokenize_text(text):
 tokens = nltk.word_tokenize(text)
 return tokens

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer(tokenizer=tokenize_text)

# Calculate cosine similarity score between two texts
def calculate_similarity(text1, text2):
 vector = vectorizer.fit_transform([text1, text2])
 return ((vector * vector.T).A)[0,1]

# Detect plagiarism based on similarity score
def detect_plagiarism(text1, text2, similarity_threshold=0.8):
 similarity_score = calculate_similarity(text1, text2)
 
 if similarity_score > similarity_threshold:
 return True
 else:
 return False