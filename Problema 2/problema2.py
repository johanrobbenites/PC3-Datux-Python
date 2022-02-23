
def ponerMayuscula(string1:str):
    lista=string1.split(' ')
    string2=""
    for i in lista:
            index=0
            p2=""
            for letras in i:
                if(index==0):
                    p2=p2+letras.upper()
                else:
                    p2=p2+letras.lower()
                index+=1
            string2+=p2
            string2+=" "
    return string2


string1=input("Ingrese una frase : ")

print("La nueva frase es : {}".format(ponerMayuscula(string1)))
