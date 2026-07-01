def find_prime_numbers(num):
    prime_numbers = []
 
    # Traverse through all numbers 
    for i in range(2, num + 1):
        count = 0
        for j in range(2, i // 2 + 1):
            if (i % j == 0):
                count += 1
                break
 
        # If the number is prime then print it 
        if (count == 0 and i != 1):
            prime_numbers.append(i)
            
    return prime_numbers