import multiprocessing
import time

def add(a, b):
 return a + b

if __name__ == '__main__':
 pool = multiprocessing.Pool()
 start = time.time()
 result = pool.apply_async(add, (2, 3))
 pool.close()
 pool.join()
 end = time.time()
 print(result.get())
 print(end-start)