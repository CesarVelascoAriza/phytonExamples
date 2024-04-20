numeros = range(10)
lista_pares =[]

for numero in numeros:
    if numero % 2 == 0:
        lista_pares.append(numero*numero)

print(f'lista pares {lista_pares}')

lista_pares = [numero * numero for numero in numeros if numero % 2 == 0]
print(f'lista de pares {lista_pares}')


pares = [numero for numero in range(50) if numero%2==0  if numero%6==0]
print(f'lista divicibles {pares}')

#agregando if el se 
lista_pares =[]
lista_impares =[]
for numero in range(10):
    if numero%2 ==0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(f'Pares : {lista_pares}')
print(f'Impares : {lista_impares}')


lista_pares =[]
lista_impares =[]
[lista_pares.append(numero) if numero %2 ==0 else lista_impares.append(numero) for numero in range(10)]
print(f'Pares : {lista_pares}')
print(f'Impares : {lista_impares}')

#lista de listas

lista_lista = [[1,2,3],[4,5,6],[7,8,9,10]]

lista_simple = [valor for sublista in lista_lista for valor in sublista]
print(f'lista simple {lista_simple}')

# sin list comprehesion

lista_pares = []
for sublista in lista_lista:
    for valores in sublista:
        if valores %2 ==0:
            lista_pares.append(valores)

print(f'lista pares {lista_pares}')

