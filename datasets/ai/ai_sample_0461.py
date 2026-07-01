def number_to_words(num):
  units = ["", "one", "two", "three", "four", "five", "six", "seven", 
           "eight", "nine"]
  teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
           "sixteen", "seventeen", "eighteen", "nineteen"]
  tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", 
          "seventy", "eighty", "ninety"]
  hundreds = ["", "onehundred", "twohundred", "threehundred", "fourhundred",
              "fivehundred", "sixhundred", "sevenhundred", "eighthundred",
              "ninehundred"]

  num_str = str(num)
  result = ""

  if num == 0:
    result = "zero"

  elif len(num_str) == 3:
    result += hundreds[int(num_str[0])] + " "
    if int(num_str[1:]) != 0:
      result += number_to_words(int(num_str[1:]))

  elif len(num_str) == 2:
    if int(num_str[0]) == 1:
      result += teens[int(num_str[1])]
    else:
      result += tens[int(num_str[0])] + " "
      if int(num_str[1]) != 0:
        result += units[int(num_str[1])]

  elif len(num_str) == 1:
    result += units[int(num_str[0])]

  return result
  
print(number_to_words(259))