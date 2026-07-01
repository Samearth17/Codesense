# Generate a list of prime numbers between 2 and 30

# Generate a list of all numbers between 2 and 30
numbers = range(2, 31)

# Loop over all numbers
for num in numbers:
    prime_flag = True
    # Check if the number is divisible by any other between 2 and itself
    for i in range(2, num):
        if (num % i == 0):
            prime_flag = False
            break
 
    # If the number is not divisible by any other number, it is prime
    if prime_flag:
        print(num)