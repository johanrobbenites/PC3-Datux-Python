class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo=largo
        self.ancho=ancho
        pass

    def area(self):
        area=self.largo*self.ancho
        return area

rectangulo1=Rectangulo(5,4)

print("El area del rectangulo 1 es : {}".format(rectangulo1.area()))

