# define a function to compute factorial 
def factorial(num): 
    if num == 0: 
        return 1
    else: 
        return num * factorial(num-1) 
  
# main program starts here 
number = int(input('Enter a number : ')) 
if number < 0: 
    print("Factorial doesn't exist for negative numbers") 
elif number == 0: 
    print("Factorial of 0 is 1") 
else: 
    print("Factorial of", number, "is", factorial(number))