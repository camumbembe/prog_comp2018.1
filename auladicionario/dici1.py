#exemploprof
frutas = [ ['laranja', 10, 1.50], ['manga', 30, 2.25], ['abacaxi', 25, 1.25], ['melancia', 15, 3.45]]

nome_fruta = input('Informe a fruta: ')

estoque_fruta = 0
valor_venda = 0

for x in range(0, len(frutas)):
	if frutas[x][0] == nome_fruta:
	estoque_fruta = frutas [x][1]
	valor_venda = frutas[x][2]
	break

print('O estoque da fruta {0} é {1} e o preço de venda é {2}'.format(nome_fruta,estoque_fruta, valor_venda)) 
