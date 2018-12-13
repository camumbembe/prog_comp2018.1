from os import system
system('cls')
import random

lista_n = []

while True:

	try:
		tamanho_lista = int(input('Informe a quantidade de itens da lista: '))

	except ValueError:
		print('O valor informado deve ser um número inteiro\n')
		continue

	else: 
		if tamanho_lista <= 0:
			print('O número deve ser maior e diferente de zero\n')
			continue
		for numeros in range(0,tamanho_lista):
			lista_n.append(random.randint(0, (tamanho_lista**2)))
		print(lista_n)
		break

while True:

	try:
		posicao = int(input('\nInforme a posição da lista que deseja acessar: '))
		print('A posição informada corresponde ao número', lista_n[posicao], 'na lista.')
		break

	except ValueError:
		print('O valor informado deve ser um numero inteiro\n')
		continue

	except IndexError:
		print('Informe um valor válido de acordo com o cumprimento da lista\n')
		continue

		
