#Generadores 
#yield para regresar los valores en el generador 
#es una funcion especia que retorna la secuencia de valores
#suspende la ejecucion segun necesite para devolver el valor del campo 

def generar():
    yield 1
    yield 2
    yield 3


#consumo a demada 

gen  = generar()

#por cada llmada consume un valor
print(next(gen))
print(next(gen))
print(next(gen))
#si se consumen mas valores de los  que produce genera un error de stop generation 

gen = generar()
for valor  in generar():
    print(f'Numero generado {valor}')