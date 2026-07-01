def capitalized(string): 
	output = []
	# Split the input string into list of words 
	words = string.split()   
	for word in words: 
		# Capitalize the first letter
		first_letter = word[0] 
		word = first_letter.upper() + word[1:] 
		output.append(word) 
        
	return " ".join(output) 

# Driver code 
string = "this is a sample sentence"
print(capitalized(string))