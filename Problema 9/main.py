import funciones as fn
def main():
    numero=fn.generarAleatorio()
    fn.intento(numero)
try:
    main()
except Exception as e:
    print(e)
