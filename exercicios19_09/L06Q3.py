
valor = int(input('Informe um número para ver seu fatorial:'))

fatorial = 1

for numero in range(valor, 0, -1):	
	
	fatorial = numero * fatorial
	
	
print('O fatorial de {0} é {1}.'.format(valor,fatorial))
