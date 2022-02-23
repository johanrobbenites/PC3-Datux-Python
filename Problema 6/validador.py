import divisor as d
def ingrese_numeros(msg:str="Ingrese las notas de la persona, divididas por comas : ") -> float:
    try:
        lista=d.dividir(msg)
        lista_notas_1=[]
        
        for notas in lista:
            numero = float(notas)
            n1=lista_notas_1.append(numero)
        print(lista_notas_1)
    except:
        print('Hay un error en el tipeo por favor introduzca bien los datos')
