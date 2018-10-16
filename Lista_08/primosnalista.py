

lista_primos = [2]
condicao = 0


for element in range(3, 101,2):
	for numero in lista_primos:
		if element % numero != 0:
			condicao = True
		else:
			condicao = False
			break
	if condicao == True:
		lista_primos.append(element)

   
print(lista_primos)
