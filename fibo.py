def Fibonacci(n):
    count = 0
    a = 0
    b = 1
    fibonacci=[]
    if(n<=0):
        return("Ingrese un numero mayor a 0")
    else:
        while count<n:
            fibonacci.append(a)
            result=a+b
            a=b
            b=result
            count+=1
        return(fibonacci)
        

num=int(input("Ingrese el numero: "))
print(Fibonacci(num))