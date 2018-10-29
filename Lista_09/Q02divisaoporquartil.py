
import random

n = int(input('Informe o valor de n: '))

lista_n = []

quartil1 = []
quartil2 = []
quartil3 = []
quartil4 = []
contador0 =contador1 = contador2 = contador3 = 0

for element in range(0, n):	
	lista_n.append(random.randint(0,99))

for element in lista_n:
    if (element <= 24):
        contador0 +=1
    if (element <= 25)  and (element <= 49):
        contador1 +=1
    if (element <= 50)  and (element <= 74):
        contador2 +=1
    if (element <= 75)  and (element <= 99):
        contador3 +=1 

print("A lista {0} \n possui: \n {1} numeros no quartil 1\n {2} numeros no quartil 2 \n {3} numeros no quartil 3 \n {4} numeros no quartil 4 \n ".format(lista_n, contador0, contador1, contador2, contador3))

#criar um for para cada quartil e verficar se os elemento estão presentes e contar quantos estão resentes


