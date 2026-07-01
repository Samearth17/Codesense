def prime_numbers(n):
    # Create an empty list to store prime numbers
    prime_list = []
    # Iterate over the numbers from 2 to n
    for num in range(2,n+1):
        prime = True
        # Iterate over the numbers from 2 to the square root of n
        for i in range(2, round(n**0.5)+1):
            # Check if num is divisible by any number
            if num % i == 0:
                prime = False
        if prime:
            prime_list.append(num)
    return prime_list

n = int(input("Enter a number: "))
print("The prime numbers between 1 and", n, "are", prime_numbers(n))