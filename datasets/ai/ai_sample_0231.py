def is_coprime(num1, num2):
        while num1 != 0 and num2 != 0: 
            if(num1 > num2): 
                num1 %= num2 
            else: 
                num2 %= num1
                  
        if(num1 == 0): 
            gcd = num2 
        else: 
            gcd = num1 
        if(gcd == 1):
            return True
        else:
            return False

if __name__ == "__main__":
    num1 = 34
    num2 = 21
    result = is_coprime(num1, num2)
    print(result)