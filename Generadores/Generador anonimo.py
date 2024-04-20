# Generador anonimo 
multiplicacion  = (valor*valor  for valor in range(4))
print(type(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))

#exprecion generadora a una funcion (sin parentecis)
import math

suma  = sum(valor*valor  for valor in range(4))
print(f'Resultado de la suma {suma}')

lista = ['juan','perez']
generador  = (valor for valor in lista)
print(next(generador))
print(next(generador))


#crear un string apartir de un generador creado a partir de una lista 
lista = ['karla', 'Gomez']
contador  = 0

def incrementar():
    global contador
    contador += 1
    return contador 

# la primea parte el yield  y la segunda es el for
generador = (f'{incrementar()}. {nombre} ' for nombre in lista)
lista = list(generador)
print(lista)

cadena = ', '.join(lista)
print(f'cadena generada {cadena}')