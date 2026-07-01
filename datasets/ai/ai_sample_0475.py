def largest_prime_in_range(start, end):
    largest_prime = 0
    # Iterate over the range
    for i in range(start, end + 1):
        # Check if number is prime
        is_prime = True
        if i > 1:
            for j in range(2, ceil(sqrt(i))+ 1):
                if i % j == 0:
                    is_prime = False
                    break
        # Check if number is the largest prime
        if is_prime and i > largest_prime:
            largest_prime = i

    return largest_prime

if __name__ == '__main__':
    output = largest_prime_in_range(3, 22)
    print(output)