def find_words_of_length_n(words, n):
    """
    Finds all words of length n.

    Parameters:
    words (list): the list of words
    n (int): the given number

    Returns:
    list: list of words of length n
    """

    result = []

    for word in words:
        if len(word) == n:
            result.append(word)

    return result