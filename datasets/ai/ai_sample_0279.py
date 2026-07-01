# Using Python

def reverseNumber(number):
    reversed = 0
    while(number > 0):
        digit = number%10
        reversed = reversed*10 + digit
        number = number//10
    
    return reversed

number = 12345
reverse = reverseNumber(number)
print(reverse) 
# Output: 54321