from Persona import Persona
from Empleado import Empleado

def main():
    persona = Persona()
    persona.id_persona(1123123)
    persona.nombre('karen')
    persona.apellido('v')
    persona.fecha_nacimiento("1/05/06")
    persona.mostrar_detalle()

#####################################################
print("Creacion objetos".center(50,'*'))
persona = Persona()
persona.id_persona=15212
persona.nombre="karen"
persona.apellido='v'
persona.fecha_nacimiento= '2024-02-02'
'''No se puede llamar el str cuando esta vacio'''
print(persona)
persona.mostrar_detalle()
del persona
empleado = Empleado(5000)
empleado.id_persona = 123123
empleado.nombre = 'la karen'
empleado.apellido = 'v'
empleado.fecha_nacimiento='2024-02-02'
print('\n')
print(f'\t\tEmpleado \nid Empleado: {empleado.id_persona} \nnombre: {empleado.nombre} - {empleado.apellido} \nsueldo: {empleado.sueldo}') 


print('\n')

#str de la clase hija 
print(empleado)
print("eliminacion de objetos".center(50,'*'))
