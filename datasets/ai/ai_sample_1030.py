def convertRoman(chars):
    # We will use a dictionary to reference Roman numerals
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 
    int_value = 0
    
    for i in range(len(chars)): # Loop through each Roman numeral
        numer = roman[chars[i]] # Get the numerical equivalent of the Roman numeral
        if (i+1)<len(chars) and roman[chars[i+1]] > numer: # Check if the Roman numeral is followed by a larger one 
            int_value -= numer # If yes, subtract the value of the numeral
        else:
            int_value += numer # Else, add it
    return int_value

chars = 'IV' 
print (convertRoman(chars))