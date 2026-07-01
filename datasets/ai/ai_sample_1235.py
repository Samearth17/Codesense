def extract_characters(str):
 # Create an empty string
 extracted = ""

 # Iterate over each character
 for char in str:
 # Check if the character is a letter
 if char.isalpha():
 # Append character to the result
 extracted += char

 # Return the extracted characters
 return extracted

# Sample input
str = "Hello world!"

# Output
print(extract_characters(str)) # Output: Helloworld