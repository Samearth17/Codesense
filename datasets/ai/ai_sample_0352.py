# Python3 code to generate an 
# array containing first n primes 
import math 

def generatePrimeArray(n): 
	prime = [True for i in range(n + 1)] 
	p = 2
	while (p * p <= n): 
		if (prime[p] == True): 
			for i in range(p * 2, n + 1, p): 
				prime[i] = False
		p += 1

	# prime[0]= False
	# prime[1]= False

	# Store prime numbers 
	prime_numbers = [] 
	for p in range(n + 1): 
		if prime[p]: 
			prime_numbers.append(p) 

	# Print the array 
	return prime_numbers 

result = generatePrimeArray(n)
print(result)