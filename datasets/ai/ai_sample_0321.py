def fibonacci_series(n): 
    # First two terms 
    a = 0
    b = 1
    c = 0
    print("Fibonacci Series:", end = " ")
    print(a , b , end = " ")
    for i in range(2,n): 
        c = a + b 
        a = b 
        b = c 
        print(c , end = " ") 

# Output should come like
# 0 1 1 2 3 5 8 13 21 34