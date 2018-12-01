
while True:
	try:
		valor = int(input('Informe um valor: '))
		valor = valor * 2
		print(valor)
		break
	except ValueError:
		print('Insira um valor inteiro')
	except KeyboardInterrupt:
		print('Ctrl + C pressionado, encerrando o programa')
		break
	
