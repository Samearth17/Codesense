import unittest 

class TestMyClassOrFunction(unittest.TestCase):

    def test_something(self):
        # Setup 
        # Code to set up a value to test 
        
        # Exercise 
        # Code for the function to test 
        result = function_to_test(*args) 
        
        # Verify
        self.assertEqual(result, expected_result) 

if __name__ == "__main__":
    unittest.main()