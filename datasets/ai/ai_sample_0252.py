import collections

def most_frequent_word(string): 
 counts = collections.Counter(string.split()) 
   
 max_count = max(counts.values()) 
   
 most_frequent = [word for word, count in counts.items() 
     if count == max_count] 
   
 print(most_frequent) 
   
if __name__ == "__main__": 
    sentence = "Code Generation is an important task in the AI research"
    most_frequent_word(sentence) 
  
# Output
# ['Generation']