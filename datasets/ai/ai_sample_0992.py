# Python program to print the first  
# 5 prime numbers 
  
# function to generate and print first  
# 5 prime numbers 
def display_first_five_primes(): 
    print("The first five prime numbers are:") 
    primenums = [2] 
    num = 3 
    while len(primenums) < 5: 
        for p in primenums: 
            if (num % p) == 0: 
                break 
        else: 
            primenums.append(num) 
        num += 1 
  
    for i in primenums: 
        print(i) 
  
# Driver code 
if __name__ == '__main__': 
    display_first_five_primes()