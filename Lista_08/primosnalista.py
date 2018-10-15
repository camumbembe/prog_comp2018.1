

lista_primos = [2]
contador = 0
posicao = 2


for element in range(3, 101,1):
    if element % lista_primos[posicao] == 0:
        contador == 0
    else:
        contador +=1
        lista_primos.append(element)

   
print(lista_primos)