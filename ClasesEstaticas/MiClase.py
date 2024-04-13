'''
variables de clase  de contexto estatico en python
y varialbes de clase 
'''

class MiClase:
    variable = 'mi variable clase'

    def __init__(self, variable_instancia) -> None:
        self.variable_instancia = variable_instancia
    
    @staticmethod
    def metodo_static():
        print(MiClase.variable)