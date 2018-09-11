numero = int(input('Informe um número para ver seu fatorial:'))
fatorial = 1

while (numero > 0):	
	
	fatorial = numero * fatorial
	
	numero = numero - 1

print(fatorial)
	
#usando o contador não é possivel imprimir o numero e o fatorial, perde-se essa capacidade. por isso são necessárias duas variáveis iniciais.
	 

