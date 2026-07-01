def int_to_Roman(number): 
  
    val = [ 
        1000, 900, 500, 400, 
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ] 
    syb = [ 
        "M", "CM", "D", "CD", 
        "C", "XC", "L", "XL", 
        "X", "IX", "V", "IV",
        "I"
        ] 
    roman_num = '' 
    i = 0
    while  number > 0:
        for_val = number // val[i]
        roman_num += syb[i] * for_val
        number -= val[i] * for_val
        i += 1
    return roman_num