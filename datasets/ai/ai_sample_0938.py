def countCommonDivisors(a,b): 
   
    divisors = [] 
   
    for i in range(1, min(a,b)+1): 
        if (a % i == 0 and b % i == 0): 
            divisors.append(i) 
              
    return len(divisors) 

num1 = 350
num2 = 400

print (countCommonDivisors(num1, num2)) 
# Output: 5