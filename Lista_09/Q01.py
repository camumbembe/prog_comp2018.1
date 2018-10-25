import random

n = int(input('Informe o valor de n: '))

lista_n = []
contador0 =contador1 = contador2 = contador3 = contador4 = contador5 = contador6 = contador7 = contador8 = contador9 = 0

for element in range(0, n):	
	lista_n.append(random.randint(0,9))

print(lista_n)

for element in lista_n:
    if element == 0:
        contador0 +=1
    if element == 1:
        contador1 +=1
    if element == 2:
        contador2 +=1
    if element == 3:
        contador3 +=1 
    if element == 4:
        contador4 +=1 
    if element == 5:
        contador5 +=1 
    if element == 6:
        contador6 +=1 
    if element == 7:
        contador7 +=1
    if element == 8:
        contador8 +=1 
    if element == 9:
        contador9 +=1


print("A lista possiu \n {0} numeros 0 \n {1} numeros 1 \n {2} numeros 2 \n {3} numeros 3 \n {4} numeros 4 \n {5} numeros 5 \n {6} numeros 6 \n {7} numeros 7 \n {8} numeros 8 \n {9} numeros 9".format(contador0, contador1, contador2, contador3, contador4, contador5, contador6, contador7, contador8, contador9))