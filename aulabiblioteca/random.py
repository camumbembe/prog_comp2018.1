import os
import random

os.system('clear')

#random - numero aletorio entre 0 e 1
#randint - gera numeros aleatorios entre os valores informados, só que inteiros
#randdom.uniform - igual ao randint so que float
#choice- escolha aleatoria dentro de uma lista informada

for contador in range(5):
	print(random())

for contador in range (1,6):
	print(random.randint(1,99))


for contador in range (1,6):
	print(random.uniform(10,20))

lista = []
for contador in range(1,51):
	lista.append(random.randint(1,99))
print(lista)
print(choice(lista))

lista1= [1,2,3,4,5,6,7,8,9]

shuffle(lista1)

print(lista1)




