"""
Optimized Python code:

import time

def foo():
    iter = 0
    max_val = 10000000
    i = 0
    while i < max_val:
        iter += i
        i += 1
    return iter

start = time.time()
foo()
end = time.time()
duration = end - start
print("Time taken: ", duration)
"""