class Persona:
    contador_personas = 0

    def __init__(self,nombre):
        self._id_persona = Persona._generar_siguente_valor()
        self._nombre = nombre
    
    @classmethod
    def _generar_siguente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas
    def __str__(self) -> str:
        return f'Persona {self._id_persona} {self._nombre }'