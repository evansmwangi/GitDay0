#Test case
import unittest
from primee import primee
class PrimeeTestCases(unittest.TestCase):
    def test_integer(self):
        with self.assertRaises(TypeError):
         prime-numbers ("String")

     def test_list(self):
          with self.assertRaises(TypeError):
           prime-numbers ("list")
    
    def test_no_negative_numbers(self):
      self.assertEqual(result, 'Invalid input', msg='Input below 0 not allowed')

    def test_it_does_not_accept_float(self):
       with self.assertRaises(ValueError) 
    
  def test_it_return_an_error_on_dict_input
        with self.assertRaises(TypeError):

    def test_divisible_by_2(self):
        self.assertEqual(primee(2), 'divisible', msg='it is not prime')

    def test_less_than_100(self):
        self.assertEqual(primee(100), 'less', msg='the prime numbers upto 100')
    def test_divisible_by_3(self):
        self.assertEqual(primee(3), 'divisible', msg='it is not prime')

   def test_input_integer_0(self):
           self.assertEqual(primee(0), 'divisible', msg='it is  prime')
  def   test_less_than_1000(self):
        self.assertEqual(primee(1000), 'less', msg='the prime numbers upto 1000')
  
