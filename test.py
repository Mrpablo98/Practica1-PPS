import unittest
from fibo import Fibonacci
#Instanciamos a clase TestFibonacci que hereda da clase unittest.TestCase
class TestFibonacci(unittest.TestCase):
    #Definimos a función do test que se asegure de que o 5 elemento da sucesión é igual a 3
    def test_quinto_elemento_fibonacci(self):
        self.assertEqual(Fibonacci(5)[4], 3)
    
#Cando se executa directamente o script test.py o seu __name__ é __main__ polo que se executa o seguinte

#Executa o código main() da clase unittest que se encarga de executar os test que se definiron anteriormente
unittest.main()
