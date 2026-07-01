from collections import Counter

def word_frequency(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Generate a dictionary to store the frequencies
    freq = dict()
 
    # Iterate over the words
    for word in words:
        if word in freq: 
            freq[word] += 1
        else: 
            freq[word] = 1

    # Use Counter to find the frequencies of words
    frequencies = Counter(freq)

    # Print the frequencies of words
    for word, frequency in frequencies.items():
        print(word + ": " + str(frequency)) 

# Driver code
sentence = "This is a test string to check the frequency of words in the string"
word_frequency(sentence)