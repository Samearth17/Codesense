def is_prime(num):
     
    # Return False if num is less than 2
    if num < 2:
        return False
     
    # Check if any number from 2 to (num - 1) divides num
    for i in range(2, num):
        if num % i == 0:
            return False
             
    else:
        return True

nums = []
num = 2

while len(nums) < 100:
    if is_prime(num):
        nums.append(num)
    num = num + 1

print(nums)