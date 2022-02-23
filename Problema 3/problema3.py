import math

class Circulo:
    def __init__(self, radio):
        self.radio=radio
        pass

    def area(self):
        area=self.radio*self.radio*math.pi
        return area

ciruclo1=Circulo(5)

print("El area del circulo1 es : {}".format(ciruclo1.area()))

