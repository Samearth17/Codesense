def most_frequent(input_string): 
  
    # split the string into words & get each word's frequency 
    splitted_string = input_string.split() 
    freq_table = {} 
    for words in splitted_string: 
        if words in freq_table: 
            freq_table[words] += 1
        else: 
            freq_table[words] = 1

 
    # find the most frequent word 
    most_freq_word = ''
    most_freq_count = 0
    for words in freq_table: 
        if freq_table[words] > most_freq_count: 
            most_freq_word = words 
            most_freq_count = freq_table[words]
  
    return most_freq_word 
  
# Driver program 
input_string = "This is a sample string"
print(most_frequent(input_string))