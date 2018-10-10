numero = '1234567890'
letra = 'QWERTYUIOPASDFGHJKLZXCVBNM'
caracter = '@#&'

conferencia = '1234567890QWERTYUIOPASDFGHJKLZXCVBNM@#&'

strSenhaPadrao = ''
contador = check = 0

while contador < 5:
	senha = input('Informe sua senha um caracter por vez:')
	strSenhaPadrao = strSenhaPadrao + senha
	contador += 1
print(strSenhaPadrao)

for strSenhaPadrao in range(5):
	if element in numero:
		check +=1
	elif element in letra:
		check +=1
	elif element in caracter:
		check +=1
	else:
		check -= 1
print(check)
		
if check > 1:
	print('')
else:
	strSenhaPadrao = input('Informe sua senha novamente:')


if len(strSenhaPadrao) != 5:
	print('Tamanho de senha inválido!')
else: 
	print('Tamanho da senha OK!')
	


 
	



