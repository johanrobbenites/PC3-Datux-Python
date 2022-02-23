def listaPalabras1(string1:str):
    lista=string1.split(' ')
    listaPalabras=[]
    for i in lista:
        if(i!=""):
            listaPalabras.append(i)
    return listaPalabras


string1=input("Ingrese una frase : ")

print("La longitude de la ultima palabra {} ".format(listaPalabras1(string1)[-1]), "es : " ,len(listaPalabras1(string1)[-1]))

