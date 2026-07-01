"""
Algorithm to determine the most common words in a given string
"""

def most_common_words(string):
    # split the string on whitespace
    words = string.split()

    # create a dictionary to store the count of each word 
    word_count = {}

    # for each word, add it to the dictionary or increment the count 
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    # convert the dictionary into a list of tuples (word, count)
    count_list = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    return count_list[0][0]

if __name__ == '__main__':
    string = 'Hello world. This is a sentence.'
    print('The most common word is:', most_common_words(string))