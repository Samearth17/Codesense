def num_common_letters(string1, string2):
    """
    Finds the number of letters that are common to two given strings
    
    Parameters:
    string1 (string): first string
    string2 (string): second string
    
    Returns:
    comm_letter_count (int): Number of letters that are common to two strings
    """
    # Initialize the variables
    comm_letter_count = 0
    
    # Iterate through the letters in the first string
    for c1 in string1:
        # Iterate through the letters in the second string
        for c2 in string2:
            # Check if the letters are the same
            if c1 == c2:
                comm_letter_count += 1
    
    return comm_letter_count

if __name__ == '__main__':
    string1 = 'Hello World'
    string2 = 'Goodbye World'
    print(num_common_letters(string1, string2))