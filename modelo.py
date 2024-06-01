def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b

def potencia(a,b):
    return a**b

def raiz(a,b):
    return a**(1/b)

def factorial(a):
    if a == 0:
        return 1
    else:
        return a*factorial(a-1)
    
print(sumar(5,3))