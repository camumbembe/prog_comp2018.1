texto = input('Informe um texto: ')

print(texto)

qt_caracteres = len(texto)

print(qt_caracteres)

texto_invertido = ''

for contador_letras in range (0, qt_caracteres):
	texto_invertido = texto[contador_letras] + texto_invertido
	
print(texto_invertido)
	
