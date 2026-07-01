import math  
  
def ArmstrongNumber(num): 
  sum = 0 
  temp_num = num 
  digits_count = 0 
  
  while temp_num>0: 
    digits_count += 1  
    temp_num = math.floor(temp_num/10)  
  
  digits_sum = 0 
    
  while num > 0:  
    r = num % 10  
    sum += math.pow(r, digits_count)  
    num = math.floor(num/10)  
      
  if sum == temp_num: 
    print (f'{temp_num} is an Armstrong number') 
  else: 
    print (f'{temp_num} is not an Armstrong number ')  
  
num = int(input("Enter a number: "))
ArmstrongNumber(num)