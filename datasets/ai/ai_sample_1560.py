def printPrime(arr): 
    for i in range (len(arr)): 
        if isPrime[arr[i]]: 
            print(arr[i], end = " ") 
          
# Function to check if a number is prime or not              
def isPrime(n): 
    # Corner case  
    if (n <= 1): 
        return False
    # Check from 2 to n-1  
    for i in range(2, n): 
        if n % i == 0: 
            return False; 
    return True

arr = [2, 3, 5, 6, 5, 7, 8, 1, 6]
printPrime(arr)