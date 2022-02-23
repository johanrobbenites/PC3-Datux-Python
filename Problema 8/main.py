import funciones as fun

def main():
    lista=[]
    fun.generarAleatorio(lista)
    fun.getLista(lista)
    fun.sorter(lista)

try:
    main()
except Exception as e:
    print(e)