def counter(text):
    """
    Function to count the occurrence of each word in the text using 
    a dictionary data structure.
    
    Parameters: 
    text (str): The given text to count.
    
    Returns: 
    dict: A dictionary of words with their counts.
    """
    result = {}  # Create empty dictionary
    for word in text.split():
        if word in result: 
            result[word] += 1
        else: 
            result[word] = 1
    return result