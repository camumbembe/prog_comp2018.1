from os import system
system('clear')
import random
import sys

ordenar = []

try:
	dados_pessoais = open('dados_pessoais.txt', 'r')
	for linha in dados_pessoais:
		dados = linha.split('#')
		ordenar.append(dados)
		print(dados)
		



except FileNotFoundError:
	print('Arquivo Inexistente')
except IndexError:
	print('O número informado não tem correspondentes na lista')
except ValueError:
	print('Informe um valor inteiro')		
except KeyboardInterrupt:
	system('clear')
	print('Programa encerrado')
		


