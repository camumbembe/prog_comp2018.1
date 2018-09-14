
frase = input('Informe uma frase e vamos contar suas palavras: ')

espaço = 1

for elemento in frase:
	if elemento == ' ':
		espaço  = espaço + 1


print('A frase tem {0} palavras.'.format(espaço))
	

