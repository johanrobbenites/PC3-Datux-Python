import math

def sumar(x:float, y:float):
    return x + y

def restar(x:float, y:float):
    return x - y

def multiplicar(x:float, y:float):
    return x * y

def dividir(x:float, y:float):
    try:
        return x /y
    except ZeroDivisionError:
        print('Division entre 0')

def potencia(x:float, y:float):
    return math.pow(x, y)
