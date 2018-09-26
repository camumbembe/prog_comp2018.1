
resposta = input('Informe seu gabarito: ')

letras = 'abcdeABCDE'

gabarito = 'ABCDEEDCBA'

comparacao = 0

while len(resposta) <= 10:
	if len(resposta) != 10:
		resposta = input('Informe o gabarito com 10 letras: ')
		
	else:
		print('Vamos analisar suas respostas')
		break

for element in resposta:	
	if element in letras:
		continue
	else:
		resposta = input('Informe o gabarito com as letras válidas: ')

print('Abaixo informaremos seu resultado')

for element in resposta.upper():
	if element in gabarito:
		print('Acerto')
		comparacao += 1
	else:
		print('Erro')
		comparacao = ''

print('Você marcou as seguintes respostas:{0}, o gabarito correto é: {1}, você acertou:{2} questões'.format(resposta, gabarito,comparacao))
