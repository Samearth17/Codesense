# Defining a function to keep track of the total number of times each word in an input string has been encountered
def count_words(input_string):
    words_dict = dict()

    for word in input_string.split():
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1

    return words_dict

# Testing the count_words() function
input_string = "This is a test string and this is a test string again"
print(count_words(input_string)) # {'This': 2, 'is': 2, 'a': 2, 'test': 2, 'string': 2, 'and': 1, 'again': 1}