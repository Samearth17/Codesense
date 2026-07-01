def printPrimeFactors(n):
    # Print the number of 2s that divide n
    while n % 2 == 0:
        print(2, end=" ")
        n = n/2
  
    # n must be odd at this point.  So we can skip
    # one element (note i = i + 2) 
    for i in range(3, int(math.sqrt(n))+1, 2):
        # While i divides n, print i and divide n
        while n % i == 0:
            print(i, end=" ")
            n = n/i
    # This condition is to handle the case when n
    # is a prime number greater than 2
    if n > 2:
        print(n, end=" ")