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

for element in strSenhaPadrao:
	if strSenhaPadrao in numero:
		check +=1
	else:
		check -= 1
print(check)
		
	


if len(strSenhaPadrao) != 5:
	print('Tamanho de senha inválido!')
else: 
	print('Tamanho da senha OK!')
	


 
	



