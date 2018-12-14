from os import system
system('clear')

lista_dados = []
postos = 'a'
lista_gasolina = lista_etanol = lista_diesels500 = lista_diesels10 = lista_gnv = []

novagasolina = []
novo_etanol = []
novo_diesels500 = []
novo_diesels10 = []
novo_gnv = []
preco_gasolina = preco_etanol = preco_diesels500 = precodiesels10 = preco_gnv = 0

precos = open('listaprecos.csv', 'r')
#separando em lista de listas
while postos:
	postos = precos.readline()
	#print(postos)	
	if  '\n' in postos:
		postos = postos[:-1]
	lista_postos = postos.split(';')
	if lista_postos != ['']:
		lista_dados.append(lista_postos)

#print(lista_dados)



#separando cada combustivel
#GASOLINA

for combustivel in lista_dados:
	if 'GASOLINA C COMUM' in combustivel:
		lista_gasolina.append(combustivel)
	preconovo = lista_gasolina[0][8].replace(',', '.')
	preco_gasolina = float(preconovo) + preco_gasolina
qt_postosgaso = len(lista_gasolina)
media_gasolina = preco_gasolina / int(qt_postosgaso)

gasolina_infos = 'GASOLINA C COMUM' + ','+ str(media_gasolina) + ',' + str(qt_postosgaso) 

novagasolina.append(gasolina_infos)
print(novagasolina)


#ETANOL
for combustivel in lista_dados:
	if 'ETANOL' in combustivel:
		lista_etanol.append(combustivel)
	preconovo = lista_etanol[0][8].replace(',', '.')
	preco_etanol = float(preconovo) + preco_etanol
print(lista_etanol)
qt_postosetanol = len(lista_etanol)

print(qt_postosetanol)
media_etanol = preco_etanol / int(qt_postosetanol)

etanol_infos = 'ETANOL' + ','+ str(media_etanol) + ',' + str(qt_postosetanol) 

novo_etanol.append(etanol_infos)
print(novo_etanol)





