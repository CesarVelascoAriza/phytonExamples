class Persona:

    def __init__(self,id,nombre,apellido,fecha):
        self.id_persona = id
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha

    
    @property
    def id_persona(self):
        return self._id_persona
    @id_persona.setter
    def id_persona(self, id):
        self._id_persona = id
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    @property
    def apellido(self):
        return self._apellido
    @nombre.setter
    def apellido(self,apellido):
        self._apellido = apellido
    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self,fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento
      
    def mostrar_detalle(self):
        print(f"Persona: {self._id_persona} , {self._nombre}, {self._apellido},{self._fecha_nacimiento}")

    def __del__(self) -> None:
        print(f'eliminando persona {self.nombre}, {self.apellido}')