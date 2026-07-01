# Import the necessary libraries 
from sklearn.model_selection import train_test_split 
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.feature_extraction.text import TfidfTransformer 
from sklearn.naive_bayes import MultinomialNB 

# Extract the data into X (text) and y (labels) 
X, y = zip(*dataset)

# Create the training and test sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0) 

# Create the count vectorizer 
count_vectorizer = CountVectorizer() 

# Transform the training and test data using count vectorizer 
X_train_counts = count_vectorizer.fit_transform(X_train) 
X_test_counts = count_vectorizer.transform(X_test) 

# Create the tf-idf transformer 
tfidf_transformer = TfidfTransformer() 

# Transform the training and test data using tf-idf 
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts) 
X_test_tfidf = tfidf_transformer.transform(X_test_counts) 

# Create the Multinomial Naive Bayes classifier and fit the data 
clf = MultinomialNB().fit(X_train_tfidf, y_train) 

# Make predictions 
predicted = clf.predict(X_test_tfidf) 

# Calculate the accuracy 
accuracy = accuracy_score(y_test, predicted) 
print("Accuracy: {0:.2f}%".format(accuracy*100))