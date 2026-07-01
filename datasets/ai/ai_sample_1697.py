import time

def time_it(func): 
    def wrapper(*args, **kwargs): 
        start = time.time() 
        result = func(*args, **kwargs) 
        end = time.time() 
        print("Execution time: {}".format(end - start)) 
        return result 
  
    return wrapper 

@time_it
def my_function(arg1, arg2):
        # Some logic code..
        return 10

my_function(10, 20)