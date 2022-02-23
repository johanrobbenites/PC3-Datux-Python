from random import randint, random


def generarAleatorio():
    numero=randint(0,100)
    return numero
def intento(numero):
    prueba=int(input("Ingrese el valor que cree que es el numero : "))
    if(prueba>numero):
        print("El numero que ingreso es mayor al que se genero")
        return(intento(numero))
    elif(prueba<numero):
        print("El numero que ingreso es menor al que se genero")
        return(intento(numero))
    else:
        print("correcto el numero es {}".format(numero))
        return
