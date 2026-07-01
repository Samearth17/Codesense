# Create a list of prime numbers between 1 and 100

def prime_nums():
    lst = [] # declare empty list
    # Iterate through the numbers from 2 to 100
    for nums in range(2, 101):
        for i in range(2, nums//2+1):
            # If any number is divisible then skip that number
            if (nums % i) == 0:
                break
        else:
            # If iteration is successful then number is prime so add in the list
            lst.append(nums)
    return lst
 
# Call the function
prime_numbers = prime_nums()
 
# Print the list of prime numbers
print(prime_numbers)