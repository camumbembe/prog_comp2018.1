

lista_primos = [2]
contador = 0
posicao = 0


for element in range(3, 101,1):
    if element % 2 != 0 and element % 3 !=0:
        lista_primos.append(element)


  
print(lista_primos)
