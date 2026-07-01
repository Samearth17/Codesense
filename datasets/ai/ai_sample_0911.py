def fibonacci(n): 
    if n == 0: return 0
    if n == 1 or n == 2: return 1

    fib_n_2 = 1
    fib_n_1 = 1
    fib_n = 0

    for i in range(3, n + 1): 
        fib_n = fib_n_1 + fib_n_2
        fib_n_2 = fib_n_1  
        fib_n_1 = fib_n 
    return fib_n 

print(fibonacci(n))