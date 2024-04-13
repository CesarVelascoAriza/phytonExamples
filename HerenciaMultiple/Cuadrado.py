from Color import Color
from FiguraGeometrica import FiguraGeometrica


class Cuadrado (FiguraGeometrica,Color):
    def __init__(self, lado,color):
        #super().__init__(lado, alto)
        FiguraGeometrica.__init__(self,lado,lado)
        Color.__init__(self,color)
    
    def calcular_area(self):
        return self._alto * self._ancho
    
    def __str__(self) -> str:
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'