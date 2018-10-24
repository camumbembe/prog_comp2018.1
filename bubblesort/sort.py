from os import system
system('clear')

import random

lista = []
for element in range(10):
    element = random.randint(1,50)
    lista.append(element)

print(lista)


n = 0


# for element in lista:
    
#     if element < lista[n]:
#         element[n], lista[n+1] = element[n+1], lista[n]    
#         print(lista)
#     n+=1

while (n < len(lista)):
    if element < lista[n]:
        element[n], lista[n+1] = element[n+1], lista[n]    
        print(lista)
    n+=1