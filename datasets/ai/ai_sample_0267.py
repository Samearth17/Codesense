import nltk
from nltk import word_tokenize

sentence = "The founder of Apple Steve Jobs passed away."

tokenized_text = word_tokenize(sentence)

tagged = nltk.pos_tag(tokenized_text)

namedEnt = nltk.ne_chunk(tagged, binary=False)

for ne in namedEnt:
 if type(ne) == nltk.tree.Tree:  
    entity_name = ' '.join(c[0] for c in ne.leaves())
    print(entity_name)