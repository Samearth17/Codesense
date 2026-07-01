# Ask the user for a number
num = int(input('Enter a number: '))

# Set initial values
is_prime = True

# Check for prime
for i in range(2, num):
 if num % i == 0:
 is_prime = False
 break

# Output result
if is_prime:
 print(f'{num} is a prime number.')
else:
 print(f'{num} is not a prime number.')