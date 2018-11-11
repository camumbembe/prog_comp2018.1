from os import system
system('clear')
import random

from inspect import currentframe, getframeinfo

cf = currentframe()
filename = getframeinfo(cf).filename


# n = int(input('Informe o valor de n: '))

lista_n = [22, 37, 15, 66, 30, 18, 76, 71, 50, 40, 1, 43, 75, 68, 82, 24, 80, 88, 92, 95, 20, 97, 35, 7, 47, 34, 27, 25, 87, 51]
# for element in range(0, 7):	
# 	lista_n.append(random.randint(0,50))

#lista_n = random.sample(range(100),30)


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
direcao_analise = 'pela_direita'

 #while aqui para repetir enquanto a esquerda for < que a len(lista_n) (e a direita?)!=0 ?

while True:
	if (direita == esquerda):
		print("\n ||||| D ==E Inicio ||||| \n Pivot: {0}, Esquerda: {1}, Direita: {2}, fim: {3}, inicio: {4}, fim_esquerda: {5}, inicio_esquerda: {6}, fim_direita: {7}, inicio_direita: {8}, direcao_analise: {9} /n" .format(pivot, esquerda, direita, fim, inicio, fim_esquerda, inicio_esquerda, fim_direita, inicio_direita, direcao_analise))
		inicio_esquerda = inicio
		fim_esquerda = esquerda -1
		if ((fim_esquerda - inicio_esquerda +1) > 1):
			esquerda = inicio_esquerda
			direita = fim_esquerda
			pivot = inicio_esquerda 
		pivot = inicio
		esquerda = inicio
		#inicio = esquerda 
		if direita > inicio_direita:
			#print('Direita: ', direita, 'Inicio Direita: ', inicio_direita)
			inicio_direita = direita +1
			#print(inicio_direita)
		direita = fim_esquerda 
		direcao_analise = 'pela_direita'
		print("\n ||||| D ==E Fim ||||| \n Pivot: {0}, Esquerda: {1}, Direita: {2}, fim: {3}, inicio: {4}, fim_esquerda: {5}, inicio_esquerda: {6}, fim_direita: {7}, inicio_direita: {8}, direcao_analise: {9} \n" .format(pivot, esquerda, direita, fim, inicio, fim_esquerda, inicio_esquerda, fim_direita, inicio_direita, direcao_analise))

	if  ((fim_esquerda - inicio_esquerda + 1) == 1) or ((fim_esquerda - inicio_esquerda + 1) == 0):
		print("\n ||||| Lenght Inicio ||||| \n Pivot: {0}, Esquerda: {1}, Direita: {2}, fim: {3}, inicio: {4}, fim_esquerda: {5}, inicio_esquerda: {6}, fim_direita: {7}, inicio_direita: {8}, direcao_analise: {9} \n" .format(pivot, esquerda, direita, fim, inicio, fim_esquerda, inicio_esquerda, fim_direita, inicio_direita, direcao_analise))
		fim_direita = fim
		pivot = inicio_direita
		esquerda = inicio_direita
		direita = fim
		#fim = direita
		inicio_esquerda = fim_esquerda + 2
		fim_esquerda = inicio_direita - 2
		#print('Direita: ', direita, 'Esquerda: ', esquerda)
		direcao_analise = 'pela_direita'
		print("\n ||||| Length Fim ||||| \n Pivot: {0}, Esquerda: {1}, Direita: {2}, fim: {3}, inicio: {4}, fim_esquerda: {5}, inicio_esquerda: {6}, fim_direita: {7}, inicio_direita: {8}, direção_analise: {9} /n" .format(pivot, esquerda, direita, fim, inicio, fim_esquerda, inicio_esquerda, fim_direita, inicio_direita, direcao_analise))
	
	if ((fim_esquerda - inicio_esquerda +1) > 1):
		esquerda = inicio_esquerda
		direita = fim_esquerda
		pivot = inicio_esquerda 

#Esquerda
	if (direcao_analise == 'pela_esquerda'):
		if lista_n[pivot] < lista_n[esquerda]:
			print('E   ', lista_n, 'Pivot: ', pivot, 'Direita: ', direita, 'Esquerda: ', esquerda, 'Line: ', cf.f_lineno)
			lista_n[pivot], lista_n[esquerda] = lista_n[esquerda], lista_n[pivot]  
			pivot = esquerda
			direcao_analise = 'pela_direita'
			print('E   ', lista_n, 'Pivot: ', pivot, 'Direita: ', direita, 'Esquerda: ', esquerda, 'Line: ', cf.f_lineno)
		else:        
			esquerda = esquerda + 1
			print('Esquerda aumentada em 1   Pivot:', pivot, 'Direita:', direita, 'Esquerda:', esquerda, 'Line: ', cf.f_lineno)
#Direita
	elif (direcao_analise == 'pela_esquerda') :
		if lista_n[pivot] > lista_n[direita]:
			print('D  ', lista_n, 'Pivot: ', pivot, 'Direita: ', direita, 'Esquerda: ', esquerda, 'Line: ', cf.f_lineno)
			lista_n[pivot], lista_n[direita] = lista_n[direita], lista_n[pivot]
			pivot = direita
			direcao_analise = 'pela_esquerda'
			print('D  ',lista_n, 'Pivot: ', pivot, 'Direita: ', direita, 'Esquerda: ', esquerda, 'Line: ', cf.f_lineno)
		else:
			direita = direita -1
			print('Direita diminuida em 1  Pivot: ', pivot, 'Direita:', direita, 'Esquerda:', esquerda, 'Line: ', cf.f_lineno)
	else:
		if lista_n[pivot] > lista_n[direita]:
			print('D  ', lista_n, 'Pivot: ', pivot, 'Direita: ', direita, 'Esquerda: ', esquerda, 'Line: ', cf.f_lineno)
			lista_n[pivot], lista_n[direita] = lista_n[direita], lista_n[pivot]
			pivot = direita
			direcao_analise = 'pela_esquerda'
			print('D  ',lista_n, 'Pivot: ', pivot, 'Direita: ', direita, 'Esquerda: ', esquerda, 'Line: ', cf.f_lineno)
		else:
			direita = direita -1
			print('Direita diminuida em 1  Pivot: ', pivot, 'Direita:', direita, 'Esquerda:', esquerda, 'Line: ', cf.f_lineno)
	print('|________________________________________________________________________________________________|')
