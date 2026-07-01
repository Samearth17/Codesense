import nltk
import re

def summarize_text(text):
 """
 A basic text summarizer that takes a text input and returns a summary of the text in two sentences.
 """

 # Tokenize the text
 tokens = nltk.sent_tokenize(text)
 # Get the frequency of each word
 word_frequencies = {}
 for word in nltk.word_tokenize(text):
 if word not in word_frequencies.keys():
 word_frequencies[word] = 1
 else:
 word_frequencies[word] += 1

 # Get the maximum frequency
 maximum_frequency = max(word_frequencies.values())

 # Compute the weight of each word
 for word in word_frequencies.keys():
 word_frequencies[word] = (word_frequencies[word]/maximum_frequency)

 # Generate the summary
 sentence_scores = {}
 for sent in tokens:
 for word in nltk.word_tokenize(sent.lower()):
 if word in word_frequencies.keys():
 if len(sent.split(' ')) < 30:
 if sent not in sentence_scores.keys():
 sentence_scores[sent] = word_frequencies[word]
 else:
 sentence_scores[sent] += word_frequencies[word]

 # Get the two highest-scoring sentences
 summary_sentences = heapq.nlargest(2, sentence_scores, key=sentence_scores.get) 

 # Construct the summary
 summary = ' '.join(summary_sentences)
 return summary