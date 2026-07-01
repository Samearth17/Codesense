# initialize the word probability counts
word_prob_dict = {}

# split the text corpus into sentences
sentences = text.split('.')

for word in words:
  word_prob_dict[word] = 0

# calculate the probability of the words appearing
for sentence in sentences:
  for word in words:
    if word in sentence:
      word_prob_dict[word] = word_prob_dict[word] + 1

for word in words:
  word_prob_dict[word] = word_prob_dict[word] / len(sentences)

print(word_prob_dict)
# Output: {'cat': 0.5, 'hat': 0.5}