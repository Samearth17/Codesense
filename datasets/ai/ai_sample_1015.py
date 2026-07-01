import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('songs.csv')

X = df[['artist', 'title', 'lyrics']]
y = df['genre'].values

# Vectorize Text
vectorizer = CountVectorizer()
X_lyrics = vectorizer.fit_transform(X['lyrics']).todense()

# Fit the model
knn = KNeighborsClassifier(5)
knn.fit(X_lyrics, y)

# Predict a genre for a new song
new_song = [['artist', 'title', 'lyrics']]
new_song_lyrics = vectorizer.transform(new_song)
predicted_genre = knn.predict(new_song_lyrics)
print(predicted_genre)