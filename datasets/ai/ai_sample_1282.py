def fibonacci_seq(n):
    if n < 0:
        raise ValueError("Index must be a positive integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return c

fib_7 = fibonacci_seq(7)
print(fib_7)