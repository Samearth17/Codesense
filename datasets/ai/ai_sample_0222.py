import unittest

def add(a, b):
    return a + b

class myTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 7), 6)

    def test_type(self):
        self.assertRaises(TypeError, add, 'a', 'b')

if __name__ == '__main__':
    unittest.main()