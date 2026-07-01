import nltk
nltk.download('punkt')
import re
from collections import defaultdict

def summarize_text(text, factor=0.2): 
 text = re.sub(r'\s+', ' ', text)

 sentences = nltk.sent_tokenize(text)
 word_counts = defaultdict(int)
 for sentence in sentences:
 for word in nltk.word_tokenize(sentence.lower()):
 word_counts[word] += 1

 top_words = sorted(word_counts, key=word_counts.get, reverse=True)[:int(len(word_counts.keys()) * factor)]
 
 summaries = []
 for sentence in sentences:
 summary = []
 for word in nltk.word_tokenize(sentence.lower()):
 if word in top_words:
 summary.append(word)
 
 summaries.append(' '.join(summary))

 return '. '.join(summaries)

summarize_text('This is a test sentence. This is another example sentence. Test sentence number 3.') // Output: This test sentence another example number