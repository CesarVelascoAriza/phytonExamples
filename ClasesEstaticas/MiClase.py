'''
variables de clase  de contexto estatico en python
y varialbes de clase 
'''

class MiClase:
    variable = 'mi variable clase'

    def __init__(self, variable_instancia) -> None:
        self.variable_instancia = variable_instancia
    
    #no se recible ninguna clase hay que realizar la instacina de la clase para poder relizar las variables de las clases
    @staticmethod
    def metodo_static():
        print(MiClase.variable)
    #recibe y puede acceder a la clase con las variables de las clases
    @classmethod
    def metodo_clase(cls):
        print(cls.variable)