def num_to_word(num):
    switcher = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty'
    }
    if num < 20:
        return switcher.get(num, 'under twenty')
    elif num < 100:
        tens = num // 10
        remainder = num % 10
        return switcher.get(tens, 'under one hundred') + ' ' + switcher.get(remainder, '')
    else:
        hundreds = num // 100
        remainder = num % 100
        return switcher.get(hundreds, 'over one hundred') + ' hundred ' + num_to_word(remainder)

print(num_to_word(123))  # Output: one hundred twenty three