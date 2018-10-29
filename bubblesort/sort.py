from os import system
system('clear')
import random

n = int(input('Informe o valor de n: '))
lista = []

for element in range(0, n):	
    lista.append(random.randint(1,50))


print(lista)


a = 1
contador = 0
condicao = True

while condicao == True:
    condicao = False
    a = 1
    for position in range(n-1):
        if lista[position] > lista[a]:
            lista[position], lista[a] = lista[a], lista[position]  
            print(lista)
            contador += 1
            condicao = True
        a += 1

print(contador)
print(lista)    

# for element in lista:
#     if element > lista[a]:
#         lista[a-1], lista[a] = lista[a], lista[a-1]  
#         print(lista)
#         contador += 1
#     a += 1
    



# while (a < len(lista)):
#     if element < lista[a]:
#         element[a], lista[a+1] = element[a+1], lista[a]    
#         print(lista)
#     a +=1 