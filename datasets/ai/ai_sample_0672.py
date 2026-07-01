def classify_words(words): 
    # Empty dictionaries 
    short_dict = {}
    long_dict = {}
    
    # Splitting the input string into words 
    word_list = words.split(", ") 
    
    # Classifying the words into two classes 
    for word in word_list: 
        if len(word) <= 7: 
            short_dict[word] = len(word) 
        else: 
            long_dict[word] = len(word) 
    
    # Return the dictionary 
    return short_dict, long_dict

# Main code     
input_string = "Luxury, Ant, Dormitory, Pro"
short_dict, long_dict = classify_words(input_string)
print(short_dict, long_dict)