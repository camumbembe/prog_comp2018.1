
quantidade = int(input('Informe quantos números da sequência de fibonacci você deseja conhecer: '))

penultimo = 0
ultimo = 1

#print(ultimo)

for elemento in range(1, quantidade+1):
	proximo = penultimo + ultimo
	penultimo = ultimo
	ultimo = proximo
	print(penultimo)
