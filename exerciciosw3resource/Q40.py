valor_A = input('Informe uma valor para A: ')
valor_B = input('Informe uma valor para B: ')
valor_C = input('Informe uma valor para C: ')

lista_valores = valor_A , valor_B , valor_C

print(lista_valores)

maior = menor = medio = lista_valores[0]

for element in lista_valores:
    if element > maior:
        maior = element
    if element < menor:
        menor = element
for element in lista_valores:
    if element < maior and element > menor:
        medio = element
  

print('A mediana é {0}.'.format(medio))