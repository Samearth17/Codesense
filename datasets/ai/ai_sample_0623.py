import random

# A list of words, that the program can use to generate lyrics
words = ["Love", "Life", "Dreams", "Happiness", "Joy", "Home",
"Friends", "Family", "Success", "Believe", "Magic", "Laughter",
"Together", "Memories", "Adventure", "Appreciate", "Peace",
"Passion", "Courage", "Forever"]

# Generate a song with 8 lines
for i in range(8):
 # Choose random words to form the line
 line = ""
 for j in range(4):
 line += random.choice(words) + " "
 # Capitalize the line and add punctuation
 line = line.capitalize() + ".\n"
 print(line)

# Print the result
print("That is all I need to be complete.")