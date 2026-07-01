import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('dataset.csv')

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], random_state=0)

vectorizer = TfidfVectorizer().fit(X_train)
X_train_vectorized = vectorizer.transform(X_train)

model = LogisticRegression(max_iter=1000).fit(X_train_vectorized, y_train)

y_pred = model.predict(vectorizer.transform(X_test))