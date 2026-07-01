import os
import collections

def create_inverted_index(documents):
    inverted_index = collections.defaultdict(list)

    for doc_id, document in enumerate(documents):
        # Go through each word in the document
        for word in document.split():
            # Add the doc_id to the entry in the inverted_index
            # for this word
            inverted_index[word].append(doc_id)

    return inverted_index

if __name__ == "__main__":
    documents = [
    "It was the best of times, it was the worst of times",
    "It was the age of wisdom, it was the age of foolishness",
    "It was the epoch of belief, it was the epoch of incredulity" 
    ]

    inverted_index = create_inverted_index(documents)
    print(inverted_index)