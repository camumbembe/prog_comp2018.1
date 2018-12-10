
frutas = { 'laranja': [10, 1.50], 
'manga': [30, 2.25], 
'abacaxi': [25, 1.25], 
'melancia': [15, 3.45]}

nome_fruta = input('informe a fruta: ').lower()

try:
	estoque_fruta = frutas[nome_fruta] [0]
	valor_venda = frutas[nome_fruta][1]

except KeyError:
	print('A fruta não consta no estoque')
except:
	print('Erro no programa')

else:
	print('O estoque da fruta {0} é {1} e o preço de venda é {2}'.format(nome_fruta,estoque_fruta, valor_venda))

finally:
	print('Fim do programa') #sempre é executado

	


 
