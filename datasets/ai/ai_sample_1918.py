# Alphabet string 
alphabets = 'abcdefghijklmnopqrstuvwxyz'

# Function to encode 
def encoding(text): 
	
	# Empty string to store encoded string 
	encoded_string = "" 

	# iterate through all characters of text 
	for i in range(len(text)): 

		# store the corresponding index 
		# of current character 
		c = alphabets.index(text[i]) 

		# append the corresponding alphabet 
		# from alphabet string 
		encoded_string += alphabets[25-c] 
	
	# Return the encoded string 
	return encoded_string 

# Function to decode 
def decoding(encoded_string): 

	# Empty string to store decoded string 
	decoded_string = "" 

	# iterate through all characters of encoded string 
	for i in range(len(encoded_string)): 

		# store the corresponding index 
		# of current character 
		c = alphabets.index(encoded_string[i]) 

		# append the corresponding alphabet 
		# from alphabet string 
		decoded_string += alphabets[25-c] 
	
	# Return the decoded string 
	return decoded_string 

# Driver code 
encoded_string = encoding("Hello World") 
print(encoded_string) 

decoded_string = decoding(encoded_string) 
print(decoded_string)