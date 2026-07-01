# Create a dictionary to store the count of each letter 
letter_counts = {}

# Loop through each letter in the given sentence
for letter in 'The quick brown fox jumps over the lazy dog.':
     # Check if the letter is present in the dictionary
     if letter in letter_counts:
         # Increment the count if the key is present
         letter_counts[letter] += 1
     else:
         # Initialize the count if the key is not present
         letter_counts[letter] = 1

# Print the output in a nice format
for key,val in letter_counts.items():
    print(key, '-', val)