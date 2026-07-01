def intToRoman(num):
 romans = ["M", "CM", "D", "CD", 
 "C", "XC", "L", "XL", 
 "X", "IX", "V", "IV", 
 "I"] 
 numbers = [1000, 900, 500, 400, 
 100, 90, 50, 40, 
 10, 9, 5, 4, 
 1] 
 res = "" 
 i = 0
 
 while num > 0: 
  # if num is greater than the number 
  # at index i, subtract the number 
  # at index i and append roman 
  # at index i in the res. 
  for _ in range(num // numbers[i]): 
   res += romans[i] 
   num -= numbers[i] 
  i += 1
 
 return res


num = 1899
print(intToRoman(num))

Output:
MDCCCXCIX