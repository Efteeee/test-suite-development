print ("Hello world")
print("Global")
print("Arshad is a goat")

from select import select
import unittest
from unittest import result
import Funtion

# The function to be tested
import Funtion



class TestFunction(unittest.TestCase):
    
    def test_addition(self):
        result = add_numbers(3,5)
        self.assertEqual(result,8)


    def test_addition_negative_numbers(self):
        result = add_numbers(-2,7)
        self.assertEqual(result,5)


    def test_addition_float_numbers(self):
        result = add_numbers(1.5,2.5)
        self.assertAlmostEqual(result,4.0,places=2)


if __name__ == '__main__':
    unittest.main()