def pascal(numero,lista2,index):
    lista3=[]
    if(numero==1):
        print([1])
    elif(numero==2):
        print([1])
        print([1,1])
    else:
        if(index==3):
            print([1])
            print([1,1])
        lista3.append(lista2[0])
        for i in range(len(lista2)-1):
           lista3.append(lista2[i]+lista2[i+1])
        lista3.append(lista2[-1])
        print(lista3)
        if(numero==index):
            return
        else:
            return pascal(numero,lista3,index+1)
def main():
    numero= int(input("Ingrese el numero de filas que desee : "))
    pascal(numero,[1,1],3)
try:
    main()
except Exception as e :
        print(e)