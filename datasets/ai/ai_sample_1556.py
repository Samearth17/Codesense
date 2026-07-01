# Function to convert a string to a list, split by words
def string_to_list(string):
    # Initialize an empty list
    word_list = []
    
    # Iterate through each character of the string
    for character in string:
        word = ""
        while character != " " and character != "":
            word += character
            string = string[1:]
            character = string[0]
        # Add each word to the list
        word_list.append(word)

    return word_list

# Driver code
my_string = "Hello world!"

word_list = string_to_list(my_string)

print(word_list) # prints ['Hello', 'world!']