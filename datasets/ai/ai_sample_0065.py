# Import the required libraries
from dataclasses import dataclass

@dataclass
class Params:
 a: int
 b: int
 c: int

def get_result(params: Params) -> int:
 """Returns the sum of the three given numbers"""
 return params.a + params.b + params.c

# Optimize the code
def optimize(fn, params):
 best_score = 0
 best_params = None
 for a in range(params.a - 10, params.a + 10):
 for b in range(params.b - 10, params.b + 10):
 for c in range(params.c - 10, params.c + 10):
 score = fn(Params(a, b , c))
 if score > best_score:
 best_score = score
 best_params = {
 'a': a,
 'b': b,
 'c': c
 }
 return best_params

if __name__ == '__main__':
 # Initialize the parameters
 params = Params(a=1, b=2, c=3)
 # Get the optimized params
 best_params = optimize(get_result, params)
 # Print the optimized result
 print("Optimized result: %d" % get_result(Params(best_params['a'], best_params['b'], best_params['c'])))