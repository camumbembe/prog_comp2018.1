listaValores = []

while True:
	valor = int(input('Informe um valor: '))
	listaValores.append(valor)
	print(listaValores)
	if (valor == 0):
		break

minimo = maximo = soma = listaValores[0]

for posicao in range(1, len(listaValores)):
	if (listaValores[posicao] > maximo):
		maximo = listaValores[posicao]
	if (listaValores[posicao] < minimo):
		minimo = listaValores[posicao]
	soma = soma + listaValores[posicao]

print(maximo, minimo, soma)



