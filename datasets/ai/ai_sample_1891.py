import pandas as pd 
import numpy as np 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# read the dataset
df = pd.read_csv('path/to/dataset/file.csv')

# feature selection
X = df[['title', 'genre', 'author', 'publisher', 'release_date', 'number_of_reviews', 'avg_rating']]

# label selection
y = np.array(df['bestseller']) 

# data preprocessing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# split data into training and test set
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size = 0.15, random_state = 0) 

# train the model
model = LogisticRegression(random_state = 0)
model.fit(X_train, y_train)

# prediction
score = model.score(X_test, y_test)

# print probability 
book_title = input("Enter the book title:") 
genre = input("Enter the genre:") 
author = input("Enter the author:") 
publisher = input("Enter the publisher:") 
release_date = int(input("Enter the release_date:")) 
number_of_reviews = int(input("Enter the number_of_reviews:")) 
avg_rating = float(input("Enter the average ratings:")) 

input_data = [[book_title, genre, author, publisher, release_date, number_of_reviews, avg_rating]]
input_data = scaler.transform(input_data)

probability = model.predict_proba(input_data)[0][1]

print('The probability of the book being a bestseller is', probability)