from os import system
system('clear')
import random
import sys

while True:
	try:
		t_lista = int(input('Informe o valor de n: '))
		if (t_lista == 0) or (t_lista < 0):
			print('Informe um inteiro válido')
			continue
		lista = []
		for element in range(0, t_lista):	
			lista.append(random.randint(0, (t_lista**2)))
		print(lista)
		break
	except ValueError:
		print('Informe um valor inteiro')
	except KeyboardInterrupt:
		system('clear')
		print('Programa encerrado')
		sys.exit()
	except:
		print('Erro no programa')

				

while True:
	try:
		posicao = int(input('Informe um numero para encontrar seu correspondente na lista: '))
		print('O correspondente na lista é: ',lista[posicao])
		break
	except IndexError:
		print('O número informado não tem correspondentes na lista')
	except ValueError:
		print('Informe um valor inteiro')		
	except KeyboardInterrupt:
		system('clear')
		print('Programa encerrado')
		sys.exit()
	except:
		print('Erro no programa')

