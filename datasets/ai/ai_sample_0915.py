def convert_to_roman(num):
    int_nums = [1000, 500, 100, 50, 10, 5, 1]
    roman_nums = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    roman_value = ''

    i = 0
    while num > 0:
        for _ in range(num // int_nums[i]):
             roman_value += roman_nums[i]
             num -= int_nums[i]
        i += 1

    return roman_value

print(convert_to_roman(99))
# Output: 'XCIX'