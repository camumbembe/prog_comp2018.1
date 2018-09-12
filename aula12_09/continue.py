
valor_n = 0

while valor_n <= 100:
	valor_n = valor_n + 1
	if (valor_n % 2 != 0):continue
#quando tem o continue ele ignora todo o resto do código  e retorno para o início do codigo, para que a condição seja satisfeita
	fatorial = valor_n
	contador = valor_n -1
	while (contador > 0):
		fatorial = fatorial * contador
		contador = contador -1
	print('{0} ! = {1}'.format(valor_n, fatorial))
	

