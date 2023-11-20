import unittest
from fibo import Fibonacci
from fibo import num
#Instanciamos a clase TestFibonacci que hereda da clase unittest.TestCase
class TestFibonacci(unittest.TestCase):
    #Definimos a función do test que se asegure de que o 5 elemento da sucesión é igual a 3.
    if num>=5:
        def test_quinto_elemento_fibonacci(self):
            esperado = 3
            resultado = Fibonacci(5)[4]
            self.assertEqual(resultado, esperado, f'A quinta posición da sucesión debería ser {esperado}, pero recibiuse: {resultado}')
    elif num<5 and num>0:
        def test_primeiro_elemento_fibonacci(self):
            esperado = 0
            resultado = Fibonacci(1)[1]
            self.assertEqual(resultado, esperado, f'A primeira posición da sucesión debería ser {esperado}, pero recibiuse: {resultado}')
    elif num>=10:
        def test_decimo_elemento_fibonacci(self):
            esperado = 34
            resultado = Fibonacci(10)[9]
            self.assertEqual(resultado, esperado, f'A decima posición da sucesión debería ser {esperado}, pero recibiuse: {resultado}')

    

#Executa o código main() da biblioteca unittest que se encarga de executar os test que se definiron anteriormente si o modulo se executa directamente e ten o nome 'main'
if __name__ == '__main__':
    unittest.main()
