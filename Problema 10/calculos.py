import operaciones as op
import validador as v

def main():
    print("Bienvenido al menú interactivo")

    print("1) Sumar dos números")
    n1 = v.ingrese_numero("Introduce el primer número: ")
    n2 = v.ingrese_numero("Introduce el segundo número: ")
    suma = op.sumar(n1, n2)  
    print(f"El resultado de la suma es: {suma}")
    print("2) Resta de dos números")
    n1 = v.ingrese_numero("Introduce el primer número: ")
    n2 = v.ingrese_numero("Introduce el segundo número: ")
    suma = op.restar(n1, n2)  
    print(f"El resultado de la resta es: {suma}")
    print("3) Multiplicacion de dos números")
    n1 = v.ingrese_numero("Introduce el primer número: ")
    n2 = v.ingrese_numero("Introduce el segundo número: ")
    suma = op.multiplicar(n1, n2)  
    print(f"El resultado de la multiplicacion es: {suma}")
    print("4) divicion de dos números")
    n1 = v.ingrese_numero("Introduce el primer número: ")
    n2 = v.ingrese_numero("Introduce el segundo número: ")
    suma = op.dividir(n1, n2)  
    print(f"El resultado de la division es: {suma}")   
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)