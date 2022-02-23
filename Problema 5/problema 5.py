class Alumno:
    def __init__(self,nombre,numero_registro):
        self.nombre=nombre
        self.numero_registro=numero_registro
        self.age=0
        self.notas=[]
        pass
    def display(self):
        print("El nombre del estudiante es {} y su numero de registro es {}".format(self.nombre,self.numero_registro))

    def setAge(self):
        edad=int(input("Ingrese la edad del alumno : "))
        self.age=edad
        
    def setNotas(self):
        nota1=int(input("Ingrese la nota 1 del alumno : "))
        nota2=int(input("Ingrese la nota 2 del alumno : "))
        nota3=int(input("Ingrese la nota 3 del alumno : "))
        self.notas.append(nota1)
        self.notas.append(nota2)
        self.notas.append(nota3)
        return self.notas

alumno1=Alumno("johan",1015510)
alumno1.setAge()
print("La edad del alumno 1 es : ",alumno1.age)

print("Las notas del alumno 1 son : ")
for i in alumno1.setNotas():
    print("La nota es: ",i)

    