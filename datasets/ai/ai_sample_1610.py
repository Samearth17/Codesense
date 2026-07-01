def string_separator(str, separator): 
    # Initialise the output list 
    output = [] 
  
    # Split the string on the set separator
    words = str.split() 
      
    # Iterate through all words in the list
    for word in words: 
  
        # Append the word along with a separator
        output.append(word + separator) 
      
    # Return the output
    return ''.join(output)