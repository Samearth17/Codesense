def int_to_Roman(number): 
  
    num = [1, 4, 5, 9, 10, 40, 50, 90, 
           100, 400, 500, 900, 1000] 
    sym = ["I", "IV", "V", "IX", "X", "XL", 
           "L", "XC", "C", "CD", "D", "CM", "M"] 
    i = 12
    while number: 
        div = number // num[i] 
        number %= num[i] 
  
        while div: 
            print(sym[i], end = "") 
            div -= 1
        i -= 1
  
# Driver Code 
if __name__ == "__main__": 
    number = 10
    int_to_Roman(number)

# Output:
X