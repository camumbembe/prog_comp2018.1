texto = input('Informe um texto: ')

print(texto)

qt_caracteres = len(texto)

print(qt_caracteres)

texto_invertido = ''
contador_letras = 0

while contador_letras < qt_caracteres:
	texto_invertido = texto[contador_letras] + texto_invertido
	contador_letras += 1

print(texto_invertido)
	

