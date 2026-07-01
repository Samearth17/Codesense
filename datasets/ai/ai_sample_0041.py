from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

# load data
samples = [
  "sample 1 from AuthorA",
  "sample 2 from AuthorA",
  "sample 1 from AuthorB",
  "sample 2 from AuthorB"
]
labels = [
  "AuthorA",
  "AuthorA",
  "AuthorB",
  "AuthorB"
]

# build the model
model = Pipeline([
  ('tfidf', TfidfVectorizer()),
  ('clf', GaussianNB())
])

# train the model
X_train, X_test, y_train, y_test = train_test_split(samples, labels, test_size=0.3)
model.fit(X_train, y_train)

# evalulate the model
score = model.score(X_test, y_test)
print(f'model score: {score}')