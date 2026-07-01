def pig_latin(string):
  vowels = ["a", "e", "i", "o", "u"]
  words = string.split()
            
  #loop through the words
  for index, word in enumerate(words):
    new_word = ""
    #check if the first letter one of the vowels 
    if word[0].lower() in vowels:
      #add the suffix 
      new_word = word + "ay"
    #otherwise move first letter to the end
    else:
      #move the first letter
      new_word = word[1:] + word[0]
      #add the suffix 
      new_word += "ay"
      
    #add the new word to list
    words[index] = new_word
            
  #return modified list
  return " ".join(words)