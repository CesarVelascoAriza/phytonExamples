from FiguraGeometrica import FiguraGeometrica
from Color import Color
class Rectangulo(FiguraGeometrica,Color):
    def __init__(self, ancho, alto, color):
        #super().__init__(ancho, alto)
        FiguraGeometrica.__init__(self,ancho,alto)
        Color.__init__(self,color)
    def calcular_area(self)->int:
        return self.alto * self.ancho
    def __str__(self) -> str:
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'