def search_smaller_word_in_larger_word(search_word, larger_word):
    """
    Searches a smaller word in a larger word
    Arguments:
        search_word -- Smaller word we have to search in the larger word
        larger_word -- Larger word
    Return: 
        True if smaller word exists in larger word, else False
    """

    if search_word in larger_word:
        return True
    return False

if __name__ == '__main__':
    search_word = "the"
    larger_word = "hello there"
    print(search_smaller_word_in_larger_word(search_word, larger_word))