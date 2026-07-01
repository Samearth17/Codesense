text = 'This is a sample string'

# Get the total number of characters 
total = len(text) 

# Count the number of vowels 
vowels = 0 
for character in text: 
 if character in 'aeiou': 
  vowels += 1

# Count the number of consonants 
consonants = 0 
for character in text: 
 if character in 'bcdfghjklmnpqrstvwxyz': 
  consonants += 1

# Print the result 
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Total: {total}")