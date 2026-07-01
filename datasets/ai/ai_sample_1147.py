import nltk

# Load the text
text = "The conference was an incredible success. All the participants were thrilled and delighted with the outcome."

# Tokenize the text
tokens = nltk.word_tokenize(text)

# Add sentiment scores to each token
scores = [0.8, 0.7, 0.7, 0.5, 0.6, 0.9, 0.2, 0.3, 0.8, 0.9, 0.9, 0.6]

# Create groups based on the sentiment scores
positive_words = list(filter(lambda x: x[1] > 0.6, zip(tokens, scores)))
neutral_words = list(filter(lambda x: 0.3 <= x[1] <= 0.6, zip(tokens, scores)))
negative_words = list(filter(lambda x: x[1] < 0.3, zip(tokens, scores)))

# Print the group results
print('Positive words:')
for word in positive_words:
 print(word[0])

print('\nNeutral words:')
for word in neutral_words:
 print(word[0])

print('\nNegative words:')
for word in negative_words:
 print(word[0])