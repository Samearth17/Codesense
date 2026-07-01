def number_to_words(num):
    units_list = {"0": "Zero", "1": "One", "2": "Two", "3": "Three", "4":
                  "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight",
                  "9": "Nine"}
    tens_list = { "10": "Ten", "11": "Eleven", "12": "Twelve", "13": "Thirteen",
                  "14": "Fourteen", "15": "Fifteen", "16": "Sixteen", "17":
                  "Seventeen", "18": "Eighteen", "19": "Nineteen", "20":
                  "Twenty", "30": "Thirty", "40": "Forty", "50": "Fifty",
                  "60": "Sixty", "70": "Seventy", "80": "Eighty", "90":
                  "Ninety"}
    
    output = ""
    if num in units_list:
        output += units_list[str(num)]
    elif num in tens_list:
        output += tens_list[str(num)]
    else:
        if len(str(num)) >= 3:
            output += units_list[str(num)[0]] + " Hundred "
            output += number_to_words(int(str(num)[1:]))
        else:
            output += tens_list[str(num)[0]+"0"] + " " 
            output += units_list[str(num)[1]]
    return output

result = number_to_words(123)
print(result)