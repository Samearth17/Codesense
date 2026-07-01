# take a number 
number = int(input("Please enter a number: ")) 
  
#initialize sum
sum = 0
  
#Find the sum of the digits of the number
temp = number
while temp > 0: 
   digit = temp % 10
   sum += digit 
   temp //= 10
  
# print the output
print("The sum of the digits of the given number is", sum)