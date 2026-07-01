def most_common_word(string):
    # convert string to lower case 
    string = string.lower() 
  
    # split the string into words  
    words = string.split() 
  
    # create a dictionary to store words and their frequency  
    word_freq_dict = {} 
  
    # iterate through each word in words list  
    for word in words: 
          
        if word not in word_freq_dict: 
            word_freq_dict[word] = 0
        word_freq_dict[word] += 1
  
    # sort the dictionary in descending order of frequency  
    sorted_dict = sorted(word_freq_dict.items(), key=lambda kv: kv[1], reverse=True) 
  
    # return the most frequent word  
    return sorted_dict[0][0]