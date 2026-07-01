def find_primes(start, end):
 # create a list of numbers
 # between start and end
 numbers = range(start, end + 1)
 
 # iterate over the list
 for i in numbers:
 # check if number is divisible
 # by any of the numbers
 # below it
 for j in range(2, i):
 if i % j == 0:
 # if yes, then remove
 # that number from the list
 numbers.remove(i)
 
return numbers
 
print(find_primes(2, 10))