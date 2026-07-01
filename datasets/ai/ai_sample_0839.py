import nltk
from nltk.tokenize import sent_tokenize

text = 'This is a sample text document. It contains some words about some things'

word_frequencies = {}
for word in nltk.word_tokenize(text):
 if word not in word_frequencies.keys():
 word_frequencies[word] = 1
 else:
 word_frequencies[word] += 1

sentences = sent_tokenize(text)
sentence_scores = {}
for sent in sentences:
 for word in nltk.word_tokenize(sent.lower()):
 if word in word_frequencies.keys():
 if len(sent.split(' ')) < 30:
 if sent not in sentence_scores.keys():
 sentence_scores[sent] = word_frequencies[word]
 else:
 sentence_scores[sent] += word_frequencies[word]
 
summary = ''
for k, v in sorted(sentence_scores.items(), key=lambda item: item[1], reverse=True)[:2]:
 summary += k + ' '

print(summary) # output: This is a sample text document. It contains some words about some things.