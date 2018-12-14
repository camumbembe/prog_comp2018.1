from os import system
system('clear')

lista_dados = []
postos = 'a'
lista_gasolina = []

lista_etanol = []
lista_diesels500 = []
lista_diesels10 = []
lista_gnv = []
lista_total = []

novagasolina = []
novo_etanol = []
novo_diesels500 = []
novo_diesels10 = []
novo_gnv = []
preco_gasolina = preco_etanol = preco_diesels500 = preco_diesels10 = preco_gnv = 0

#abrindo o arquivo no modo leitura
precos = open('listaprecos.csv', 'r')

#separando em lista de listas usando readline
while postos:
	postos = precos.readline()
	#print(postos)	
	if  '\n' in postos:
		postos = postos[:-1]
	lista_postos = postos.split(';')
	if lista_postos != ['']:
		lista_dados.append(lista_postos)

#print(len(lista_dados))



#separando cada combustivel
#GASOLINA
for combustivel in lista_dados:
	if 'GASOLINA C COMUM' in combustivel:
		lista_gasolina.append(combustivel)
		preconovo = lista_gasolina[0][8].replace(',', '.')
		preco_gasolina = float(preconovo) + preco_gasolina
qt_postosgaso = len(lista_gasolina)
media_gasolina = preco_gasolina / int(qt_postosgaso)

gasolina_infos = 'GASOLINA C COMUM' + ', '+ str(media_gasolina) + ', ' + str(qt_postosgaso) 

novagasolina.append(gasolina_infos)
print(novagasolina)


#ETANOL
for combustivel in lista_dados:
	if 'ETANOL' in combustivel:
		lista_etanol.append(combustivel)
		preconovo = lista_etanol[0][8].replace(',', '.')
		preco_etanol = float(preconovo) + preco_etanol
#print(len(lista_etanol))

qt_postosetanol = len(lista_etanol)

media_etanol = preco_etanol / int(qt_postosetanol)

etanol_infos = 'ETANOL' + ', '+ str(media_etanol) + ', ' + str(qt_postosetanol) 

novo_etanol.append(etanol_infos)
print(novo_etanol)

#DIESEL S500

for combustivel in lista_dados:
	if 'DIESEL S500' in combustivel:
		lista_diesels500.append(combustivel)
		preconovo = lista_diesels500[0][8].replace(',', '.')
		preco_diesels500 = float(preconovo) + preco_diesels500


qt_postosdiesels500 = len(lista_diesels500)

media_diesels500 = preco_diesels500 / int(qt_postosdiesels500)

diesels500_infos = 'DIESEL S500' + ', '+ str(media_diesels500) + ', ' + str(qt_postosdiesels500) 

novo_diesels500.append(diesels500_infos)
print(novo_diesels500)

#DIESEL S10
for combustivel in lista_dados:
	if 'DIESEL S10' in combustivel:
		lista_diesels10.append(combustivel)
		preconovo = lista_diesels10[0][8].replace(',', '.')
		preco_diesels10 = float(preconovo) + preco_diesels10


qt_postosdiesels10 = len(lista_diesels10)

media_diesels10 = preco_diesels10 / int(qt_postosdiesels10)

diesels10_infos = 'DIESEL S10' + ', '+ str(media_diesels10) + ', ' + str(qt_postosdiesels10) 

novo_diesels10.append(diesels10_infos)
print(novo_diesels10)

#GNV
for combustivel in lista_dados:
	if 'GNV' in combustivel:
		lista_gnv.append(combustivel)
		preconovo = lista_gnv[0][8].replace(',', '.')
		preco_gnv = float(preconovo) + preco_gnv

qt_postosgnv = len(lista_gnv)

media_gnv = preco_gnv / int(qt_postosgnv)

gnv_infos = 'GNV' + ', '+ str(media_gnv) + ', ' + str(qt_postosgnv)

novo_gnv.append(gnv_infos)
print(novo_gnv)


#compilado_postos = gasolina_infos + etanol_infos
#lista_total.append(element)
#print(lista_total)
		

precos.close()

