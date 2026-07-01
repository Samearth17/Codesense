import nltk
from nltk.corpus import brown
from nltk.tokenize import word_tokenize 

# Train and test data 
train_data = brown.tagged_sents(categories='news') 
test_data = brown.sents(categories='news') 
  
# Build our POS Tagger 
tagger = nltk.UnigramTagger(train_data, backoff = nltk.DefaultTagger('NN')) 

def check_voice(sentence):
  tokens = word_tokenize(sentence)
  tagged_sent = tagger.tag(tokens) 
  if tagged_sent[0][1] == 'VBN':
    return 'Passive'
  else:
    return 'Active'

>>>check_voice('The work was done by John.')
'Passive'