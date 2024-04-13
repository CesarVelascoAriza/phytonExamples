class Persona:
    contador_personas = 0

    def __init__(self,nombre):
        Persona.contador_personas +=1
        self._id_persona = Persona.contador_personas
        self._nombre = nombre
    def __str__(self) -> str:
        return f'Persona {self._id_persona} {self._nombre }'