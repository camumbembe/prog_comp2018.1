
palavra = input('Informe uma palavra e vamos contar suas vogais e consoantes: ')

todasvogais = 'AEIOUaeiouãõÃÕàáéíóúÁÉÍÓÚâêîôû'
vogais = consoantes = numero = quantidade = 0

for letra in palavra:
	numero = numero + 1
print(numero)


while quantidade > numero:
	if palavra in todasvogais:
		vogais = vogais + 1
	else:
		consoantes = consoantes + 1
	quantidade = quantidade + 1

print('Vogais = {0} e Consoantes = {1}'.format(vogais,consoantes))
