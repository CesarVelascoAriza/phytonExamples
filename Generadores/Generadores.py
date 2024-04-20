#generador de nuemeros 1 a 5 
def generador_numeros():
    for numero  in range(1,6):
        yield numero
        print('se reanuda la ejecucion de la funcion')


#utilizamos el generador 
generador = generador_numeros()
print(f'Objeto generador :> {generador}  tipo {type(generador)}')

##
for valor in generador_numeros():
    print(f'validar el valor {valor}')



try:
    generador = generador_numeros()
    while True:
        valor = next(generador)
        print(f'valor generador while {valor}')
except StopIteration as e:
    print('se termina el generador ')