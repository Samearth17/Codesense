def is_prime(n):
 # check if n is divisible by any of the numbers
 # between 2 and n-1
 for i in range(2, n):
 if n % i== 0:
 return False

 return True 

def check_lst(lst):
 # generate a list of booleans 
 # where each element corresponds to the corresponding
 # element of lst
 result_lst = []
 for i in range(len(lst)):
 if is_prime(lst[i]):
 result_lst.append(True)
 else:
 result_lst.append(False)

 return result_lst

lst = [7, 8, 12, 19, 22, 23]
print(check_lst(lst))

# Output: 
# [True, False, False, True, False, True]