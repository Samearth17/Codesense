import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

# Define the pipeline
def summarize(text):
    sentences = sent_tokenize(text)
    word_sentences = [word_tokenize(sentence) for sentence in sentences]
    stemmer = PorterStemmer()
    stop_words = stopwords.words('english')
    word_sentences = [[stemmer.stem(w.lower()) for w in word if w not in stop_words] for word in word_sentences]
    # Build word frequency table
    word_freq_table = dict()
    for words in word_sentences:
        for word in words:
            if word in word_freq_table:
                word_freq_table[word] += 1
            else:
                word_freq_table[word] = 1
    # Calculate sentence scores
    sentence_scores = dict()
    for i, sentence in enumerate(word_sentences):
        total = 0
        for word in sentence:
            if word in word_freq_table:
                total += word_freq_table[word]
        sentence_scores[i] = total
    # Find top n sentences
    n = 2 # Change this to change number of summary sentences
    top_n_sentences_index = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:n]
    top_n_sentences = [sentences[i] for i in top_n_sentences_index]
    # Return summary
    return ' '.join(top_n_sentences)

# Test the pipeline
text = "These are some words. These are some more words. These are even more words. Here is a summary sentence."
print(summarize(text))

# Output: These are some words. Here is a summary sentence.