from abc import ABC,abstractmethod
class FiguraGeometrica(ABC):
    def __init__(self,ancho,alto) -> None:
        self._ancho =ancho
        self._alto =alto

    @property
    def ancho(self):
        return self._ancho
    #dejar los elementos de solo lectura
    #@ancho.setter
    #def ancho(self, ancho):
    #    self._ancho =ancho
    
    @property
    def alto(self):
        return self._alto
   #Dejar atributos de solo lectura
   # @alto.setter
   # def alto(self, alto):
   #     self._alto =alto

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self) -> str:
        return f'\t\tFiguraGeometrica \n Ancho: {self._ancho} \n Alto: {self._alto}' 