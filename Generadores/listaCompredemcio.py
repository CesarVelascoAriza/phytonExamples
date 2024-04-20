numeros = range(10)
lista_pares =[]

for numero in numeros:
    if numero % 2 == 0:
        lista_pares.append(numero*numero)

print(f'lista pares {lista_pares}')

lista_pares = [numero * numero for numero in numeros if numero % 2 == 0]
print(f'lista de pares {lista_pares}')
