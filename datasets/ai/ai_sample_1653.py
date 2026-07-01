import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# sample emails
emails = [
"Hey, I'm offering a 50% discount on our services!",
"Did you see the latest news about the software update?",
"Do you want to make money fast and easy?",
"Please save the date for our upcoming event on April 15th.",
"You have one last chance to get this limited offer!"
]

labels = [1, 0, 1, 0, 1]

# pre-process the emails
email_words = []
for email in emails:
 email_words.append(' '.join(nltk.word_tokenize(email)))

# feature extraction
vectorizer = CountVectorizer()
features = vectorizer.fit_transform(email_words)

#naive bayes calssifier
classifier = MultinomialNB()
classifier.fit(features, labels)

# test the model
test_email = "Will you join us at the upcoming meeting?”
test_email_words = ' '.join(nltk.word_tokenize(test_email))
test_features = vectorizer.transform([test_email_words])

# predict the class
print(classifier.predict(test_features))  # output: [0] - non-spam email