import unittest
from fibo import Fibonacci
#Instanciamos a clase TestFibonacci que hereda da clase TestCase
class TestFibonacci(unittest.TestCase):
    #Definimos a función do test que se asegure de que o 5 elemento da sucesión é igual a 3
    def test_quinto_elemento_fibonacci(self):
        result=Fibonacci(5)
        self.assertEqual(result[4], 3)