def find_occurrences(sentence):
    # Empty list to store indices of occurrence
    indices = []

    # get length of sentence
    l = len(sentence)
 
    # iterate to go through the sentence
    for i in range(l):
        # if at any point a substring from i to i+3 is equal to "cat"
        if sentence[i:i+3] == "cat":
            # add i to list of indices
            indices.append(i)
 
    # return the list of indices
    return indices

occurrences = find_occurrences("The cat sat on the mat.")
print("Indices of occurrences:", occurrences)