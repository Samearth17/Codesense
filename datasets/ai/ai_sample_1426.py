def highest_scoring_word(text): 
    
    # Split the text into words 
    words = text.split() 
  
    # Create a dictionary to store the words 
    # and their corresponding scores 
    scores = {} 
    for word in words: 
        score = 0
        for letter in word: 
            score += ord(letter) - 96 
        scores[word] = score 
  
    # Find the highest score 
    highest_score = 0
    for key, value in scores.items(): 
        if value > highest_score: 
            highest_score = value 
            highest_scoring_word = key 
  
    return highest_scoring_word

# Driver code
text = "The cat runs fast"
print(highest_scoring_word(text))