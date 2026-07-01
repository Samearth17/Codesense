#import the python testing library
import unittest

#import the function to be tested
from mycode import myfunction

# Create an instance of the test
test = unittest.TestCase()  

# Create a list of inputs to test
inputs = [[1,2], [3,4], [5,6]]

# Create expected outputs
expected_outputs = [3, 7, 11]

# Check the outputs for all inputs 
for i in range(len(inputs)):  
     result = myfunction(inputs[i][0], inputs[i][1])
     test.assertEqual(result, expected_outputs[i])