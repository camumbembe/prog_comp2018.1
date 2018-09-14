
palavra = input('Informe uma palavra e vamos contar suas vogais e consoantes: ')

vogais = consoantes = 0

for letra in palavra:
	if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
		vogais = vogais + 1
	else:
		consoantes = consoantes + 1

print('Vogais = {0} e Consoantes = {1}'.format(vogais,consoantes))


