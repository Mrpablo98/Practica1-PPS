def Fibonacci(n):
    #Se inicializan as variables 'a' e 'b' cos 2 primeiros valores da sucesión fibonacci.
    a = 0
    b = 1
    #Inicializamos un array no que se gardará o resultado da sucesión.
    fibonacci=[]
    #Si o número introducido é negativo non se pode realizar a sucesión.
    if(n<=0):
        return("Ingrese un numero mayor a 0")
    else:
    #Mentres a conta sea inferior ao número introducido volvera a executarse a suma máis a reasignación das variables 'a=b' e 'b=result(a+b)'.
        for i in range(0, n):
            fibonacci.append(a)
            result=a+b
            a=b
            b=result
        return fibonacci

num=int(input("Introduce un numero: "))
print(Fibonacci(num))

