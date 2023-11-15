def Fibonacci(n):
    #Inicializamos a variable 'count' para contar as veces que se repite o bucle.
    count = 0
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
        while count<n:
            fibonacci.append(a)
            result=a+b
            a=b
            b=result
            #Incrementamos a conta en 1.
            count+=1
        return(fibonacci)
        


