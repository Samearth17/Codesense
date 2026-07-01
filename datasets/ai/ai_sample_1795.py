def roman_to_int(roman):
    # Create a dictionary for the Roman numerals
    roman_values = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    total = 0
    for i in range(len(roman)):
        # If the current value is greater than the previous value, subtract it from the total
        if i != 0 and roman_values[roman[i]] > roman_values[roman[i-1]]:
            total -= roman_values[roman[i-1]]
        # Add the current value to the total
        total += roman_values[roman[i]]

    return total

num = roman_to_int('MCMLIV')
print(num)