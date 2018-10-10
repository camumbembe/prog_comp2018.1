listaValores = []

while True:
	valor = int(input('Informe um valor: 0'))
	listaValores.append(valor)
	print(listaValores)
	if (valor == 0):
		break

listaValores.pop()
print(listaValores)

listaValores.pop(2)
print(listaValores)

listaValores.insert(2, -55) #primeiro a posicao depois o que se deseja acrescentar, pode ser um input
print(listaValores)

