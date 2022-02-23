numero=input("Ingrese el numero de la tarjeta de credito : ")
numero2=numero[::-1]
suma_parcial1=0
suma_parcial2=0
suma_total=0
valores=[]
indice=0
for i in numero2:
    if indice%2==0:
        suma_parcial2+=int(i)
    else:
        valores.append(int(i)*2)
    indice+=1
for j in valores:
     if(j>=10):
         suma_parcial2+=(j%10)+1
     else:
         suma_parcial2+=j
suma_total=suma_parcial1+suma_parcial2
if(suma_total%10==0):
    if numero[0:2]=="51" or numero[0:2]=="52" or numero[0:2]=="53" or numero[0:2]=="54" or numero[0:2]=="55" :
        print("MASTERCARD\n")
    if numero[0:2]=="34" or numero[0:2]=="37":
        print("AMEX\n")
    if numero[0]=="4":
        print("VISA\n")
else:
    print("INVALID\n")