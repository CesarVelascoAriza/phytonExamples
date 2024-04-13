from Persona import Persona

class Empleado(Persona):
    def __init__(self,sueldo):
        super()
        self._sueldo = sueldo
    @property
    def sueldo(self):
        return self._sueldo
    @sueldo.setter
    def sueldo(self,sueldo):
        self._sueldo=sueldo
    def __str__(self):
        return f'{super().__str__()} {self.sueldo}'