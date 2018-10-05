texto = input('Informe um texto: ')

print(texto)

qt_caracteres = len(texto)

print(qt_caracteres)

texto_invertido = ''

for contador_letras in texto:
	texto_invertido = contador_letras + texto_invertido
	
print(texto_invertido)
	
