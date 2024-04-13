from Persona import Persona

class Empleado(Persona):
    def __init__(self,id,nombre,apellido,fecha,sueldo):
        super().__init__(id,nombre,apellido,fecha)
        self._sueldo = sueldo
    @property
    def sueldo(self):
        return self._sueldo
    @sueldo.setter
    def sueldo(self,sueldo):
        self._sueldo=sueldo