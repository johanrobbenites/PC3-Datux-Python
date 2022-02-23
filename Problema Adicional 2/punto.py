import math
class Punto:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def string(self):
        print("Las corrdenadas del punto son {} , {} ".format(self.x,self.y))
    def cuadrante(self):
        if self.x==0 and self.y!=0 :
            print("Esta situado en el Eje Y")
        elif self.x!=0 and self.y==0 : 
            print("Esta situado en el Eje X")
        elif self.x==0 and self.y==0 : 
            print("El punto es el Origen de coordenadas")
        elif self.x>0 and self.y>0 : 
            print("El punto esta situado en el Cuadrante 1")
        elif self.x<0 and self.y>0 : 
            print("El punto esta situado en el Cuadrante 2")
        elif self.x<0 and self.y<0 : 
            print("El punto esta situado en el Cuadrante 3")
        elif self.x>0 and self.y<0 : 
            print("El punto esta situado en el Cuadrante 4")
    
    def vector(self, puntos):
        print("El vector es ({}, {})".format(puntos.x - self.x, puntos.y - self.y) )
    def distancia(self, punto):
        d=math.sqrt(pow(abs(punto.x - self.x),2) + pow(abs(punto.y - self.y),2))
        print("La distancia es : {}".format(d))

class Rectangulo:
    def __init__(self,pi=Punto(),pf=Punto()):
        self.pi = pi
        self.pf = pf
        self.cBase = abs(self.pf.x - self.pi.x)
        self.cAltura = abs(self.pf.y - self.pi.y)
        self.cArea = self.cBase * self.cAltura
    def Base (self):
        print("La base del rectangulo es : {}".format(self.cBase))

    def Altura (self):
        print("La base del rectangulo es : {}".format(self.cAltura))
    
    def Area (self):
        print("La base del rectangulo es : {}".format(self.cArea))
# Testing Punto
A=Punto(2,3)
B=Punto(5,5)
C=Punto(-3,-1)
D=Punto(0,0)
A.cuadrante()
C.cuadrante()
D.cuadrante()
A.vector(B)
B.vector(A)

rectangulo1=Rectangulo(A,B)
rectangulo1.Base()
rectangulo1.Altura()
rectangulo1.Area()