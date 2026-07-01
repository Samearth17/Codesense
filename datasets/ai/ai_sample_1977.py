import pandas as pd 

# Preparation of data
# Fetch articles from news sources
# Create a dataframe from the articles
# Split into training and test data

df = pd.DataFrame({
'Text': ['NASA unveiled the Mars 2020 mission on Wednesday, a rover that will search for traces of ancient Martian life while performing geological studies of the red planet.'],
'Label': ['technology']
})

train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

# Create a model using a random forest classifier

model = RandomForestClassifier(n_estimators=100)

# Extract features from the articles

vectorizer = TfidfVectorizer(stop_words='english')
vectorizer.fit(train_data.Text)

X_train = vectorizer.transform(train_data.Text)
X_test = vectorizer.transform(test_data.Text)

# Train the model

model.fit(X_train, train_data.Label)

# Evaluate the model

print(model.score(X_test, test_data.Label))

# Make a prediction

prediction = model.predict(X_test)
print(prediction)