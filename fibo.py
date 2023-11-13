def Fibonacci(n):
    #variable count para contar as veces que se repite o bucle.
    count = 0
    #a e b inicializan os 2 primeiros valores da sucesión fibonacci
    a = 0
    b = 1
    #inicializamos un aray no que se guardara o resultado da sucedión
    fibonacci=[]
    #Si o numero introducido e negativo non se pode realizar a sucesión
    if(n<=0):
        return("Ingrese un numero mayor a 0")
    else:
    #mentres a conta sea inferior ao numero introducido volvera a executarse a suma e a reasignación das variables a=b e b= ao resultado da suma anterior
        while count<n:
            fibonacci.append(a)
            result=a+b
            a=b
            b=result
            count+=1
        return(fibonacci)
        


