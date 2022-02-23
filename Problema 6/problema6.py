import validador as v

def main():
    mensaje=input("Ingrese las notas de la persona, divididas por comas : ")
    v.ingrese_numeros(mensaje)
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)