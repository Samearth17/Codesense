def num_to_words(num):
    basic_terms = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }
    
    if num in basic_terms.keys():
        return basic_terms[num]

    else:
        num_words = ""
        if num > 20 and num < 100:
            num_words += basic_terms[num - (num % 10)] + " "
                         + basic_terms[num % 10]
        elif num >= 100 and num < 1000:
            num_words += basic_terms[num // 100] + " " + "hundred " 
            if num % 100 != 0:
                num_words += num_to_words(num % 100)
        elif num >= 1000 and num < 10000:
            num_words += basic_terms[num // 1000] + " " + "thousand " 
            if num % 1000 != 0:
                num_words += num_to_words(num % 1000)
    return num_words