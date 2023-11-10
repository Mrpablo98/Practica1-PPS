import unittest
from fibo import Fibonacci

class TestFibonacci(unittest.TestCase):
    def test_quinto_elemento_fibonacci(self):
        result=Fibonacci(5)
        self.assertEqual(result[4], 3)