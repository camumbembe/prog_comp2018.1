numero = int(input('Informe um número: '))
soma = 0 
contador = 0 

while numero != 0:
	contador = contador + 1
	soma = soma + numero
	numero = int(input('Informe um número: '))
	
media = soma // contador
print('A soma dos números digitados é: ', soma, ' e a média é: ', media)