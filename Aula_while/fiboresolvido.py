quantidade = int(input('Informe quantos números da sequência de fibonacci você deseja conhecer: '))

penultimo = 0
ultimo = 1

print(ultimo)

while (quantidade > 1):

	proximo = penultimo + ultimo
	print(proximo)
	penultimo = ultimo
	ultimo = proximo
	quantidade = quantidade -1 






