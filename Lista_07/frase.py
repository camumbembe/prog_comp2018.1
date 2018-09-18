
frase = input('Informe uma frase e vamos contar suas palavras: ')

espaco = 1

for elemento in frase:
	if elemento == ' ':
		espaco  = espaco + 1


print('A frase tem {0} palavras.'.format(espaco))
	

