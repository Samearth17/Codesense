# Python program to generate all prime numbers between two given numbers 
  
def generate_prime_numbers(low,high): 
    if low == 1: 
        low += 1
    for num in range(low,high + 1):    # Iterating over the range 
        if num > 1: 
            for i in range(2,num): 
                if (num % i) == 0: 
                    break 
            else: 
                print(num) 
  
low = 1
high = 10

generate_prime_numbers(low,high)