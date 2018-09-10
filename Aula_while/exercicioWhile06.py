numero = int(input('Informe um número: '))
soma =  contador = 0 

while numero != 0:
	contador = contador + 1
	soma = soma + numero
	numero = int(input('Informe um número: '))

if numero != 0:
	media = soma // contador

print('A soma dos números digitados é: {0} e a média é: {1}' .format(soma, media))
