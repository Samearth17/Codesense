# define a dictionary of Roman Numerals to Arabic numbers
roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def roman_to_arabic(roman_string):
    total = 0
    #Split the Roman number into characters
    chars = [char for char in roman_string]

    #If the length of the Romans is 0, return 0
    if (len(chars)==0):
        return 0

    # Start from the end
    x = len(chars)-1

    #Stores previous character
    last_char = 'I'

    #Loop through all characters of string
    while (x>=0):
        #Store current character
        current_char = chars[x]

        #Check if the current character is greater than or equal to last character
        if (current_char == last_char or roman[current_char]<=roman[last_char]):
            total+=roman[current_char]

        else:
            total-=roman[current_char]

        last_char = current_char
        x-=1

    return total

#Convert MCMXCVIII to Arabic numbers
print(roman_to_arabic('MCMXCVIII'))  # Output: 1998