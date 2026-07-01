import nltk

# Training data
names = [("Amy", "female"), ("Booker", "male"), ("Charles", "male"), ("Daisy", "female")]

# Feature extraction
def gender_features(name):
 features = {}
 features["first_letter"] = name[0].lower()
 features["last_letter"] = name[-1].lower()
 return features

# Feature set
feature_set = [(gender_features(name), gender) for (name, gender) in names]

# Classifier 
classifier = nltk.NaiveBayesClassifier.train(feature_set)

# Test 
print(classifier.classify(gender_features('Amy')))   # female
print(classifier.classify(gender_features('Booker'))) # male
print(classifier.classify(gender_features('Charles'))) # male
print(classifier.classify(gender_features('Daisy')))  # female