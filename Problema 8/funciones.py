from random import randint
def generarAleatorio(lista=[]):
    for i in range(5):
        numero = randint(0,100)
        lista.append(numero)
    return lista
def getLista(lista):
    print(lista)
def sorter(lista):
    print(sorted(lista))
