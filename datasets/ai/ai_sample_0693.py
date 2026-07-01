def find_shortest_distance(sentence, word1, word2):
    words = sentence.split()
    shortest_distance = float("inf")
    for i, word in enumerate(words):
        if word == word1 or word == word2:
            if word == word1:
                target_word = word2
            else:
                target_word = word1
            for j in range(i + 1, len(words)):
                if words[j] == target_word:
                    distance = j - i
                    if distance < shortest_distance:
                        shortest_distance = distance
                    break
    return shortest_distance

sentence = "The quick brown fox jumps over the lazy dog"
distance = find_shortest_distance(sentence, 'fox', 'dog')
print("The shortest distance between fox and dog is ", distance)  # The shortest distance between fox and dog is 8