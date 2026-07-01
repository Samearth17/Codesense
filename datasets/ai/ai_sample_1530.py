def is_prime(num):
    #Ignore negative numbers and zero
    if num < 2:
        return False
    
    #Return true if num is prime
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

#Print all prime numbers between 0 and a given number
num_input = int(input("Enter a number: "))
for i in range(num_input):
    if is_prime(i):
        print(i, "is a prime number")