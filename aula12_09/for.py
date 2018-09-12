

for valor_n in range(0, 101, 2):
	fatorial = valor_n
	for contador in range(valor_n - 1, 1, -1):
		fatorial = fatorial * contador
	print('{0}! = {1}'.format(valor_n, fatorial))

