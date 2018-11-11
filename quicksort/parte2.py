from os import system
system('cls')
import random

from inspect import currentframe, getframeinfo

cf = currentframe()
filename = getframeinfo(cf).filename
print("This is line 5, python says line ", cf.f_lineno )

# n = int(input('Informe o valor de n: '))

lista_n = [44,35,26,91,6,64,52,4,32,50]
# for element in range(0, 7):	
# 	lista_n.append(random.randint(0,50))

#lista_n = random.sample(range(100),10)


print(lista_n)

pivot = 0
esquerda = 0
direita = len(lista_n) - 1
fim = len(lista_n) - 1
inicio = 0
fim_esquerda = len(lista_n) - 1
inicio_esquerda = 0
fim_direita = len(lista_n) - 1
inicio_direita = 0
 #while aqui para repetir enquanto a esquerda for < que a len(lista_n) (e a direita?)!=0 ?

while True:
	if (direita == esquerda):
		inicio_esquerda = inicio
		fim_esquerda = esquerda -1
		pivot = inicio
		esquerda = inicio
		if direita > inicio_direita:
			print('Direita: ', direita, 'Inicio Direita: ', inicio_direita)
			inicio_direita = direita +1
			print(inicio_direita)
		direita = fim_esquerda

	if  ((fim_esquerda - inicio_esquerda + 1) == 1) or ((fim_esquerda - inicio_esquerda + 1) == 0):
		
		fim_direita = fim
		pivot = inicio_direita
		esquerda = inicio_direita
		direita = fim
		fim_esquerda = 10
		inicio_esquerda = 0
		print('Direita: ', direita, 'Esquerda: ', esquerda)
#Esquerda
	if (pivot > (len(lista_n) //  2)) or (pivot == direita):
		if lista_n[pivot] < lista_n[esquerda]:
			lista_n[pivot], lista_n[esquerda] = lista_n[esquerda], lista_n[pivot]  
			pivot = esquerda
			print(lista_n, 'Pivot: ', pivot, 'Direita: ', direita, 'Esquerda: ', esquerda, 'Line: ', cf.f_lineno)
		else:        
			esquerda = esquerda + 1
			print(lista_n, 'Pivot: ', pivot, 'Direita: ', direita, 'Esquerda: ', esquerda, 'Line: ', cf.f_lineno)
#Direita
	elif (pivot < (len(lista_n) //  2)) or (pivot == esquerda):
		if lista_n[pivot] > lista_n[direita]:
			lista_n[pivot], lista_n[direita] = lista_n[direita], lista_n[pivot]
			pivot = direita
			print(lista_n, 'Pivot: ', pivot, 'Direita: ', direita, 'Esquerda: ', esquerda, 'Line: ', cf.f_lineno)
		else:
			direita = direita -1
			print(lista_n, 'Pivot: ', pivot, 'Direita: ', direita, 'Esquerda: ', esquerda, 'Line: ', cf.f_lineno)
	else:
		if lista_n[pivot] < lista_n[esquerda]:
			lista_n[pivot], lista_n[esquerda] = lista_n[esquerda], lista_n[pivot]  
			pivot = esquerda
			print(lista_n, 'Pivot: ', pivot, 'Direita: ', direita, 'Esquerda: ', esquerda, 'Line: ', cf.f_lineno)
		else:        
			esquerda = esquerda + 1
			print(lista_n, 'Pivot: ', pivot, 'Direita: ', direita, 'Esquerda: ', esquerda, 'Line: ', cf.f_lineno) 
	# print('Fimm Direita: ', direita, 'Inicio Direita: ', inicio_direita)
