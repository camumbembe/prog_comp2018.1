from os import system
system('clear')

lista_dados = []
lista_combustiveis = []
gasolina = []
separando_linha = 'a'
preco_combustiveis = open('listaprecos.csv', 'r')

while separando_linha:
    separando_linha = preco_combustiveis.readline()
    if  '\n' in separando_linha:
	    separando_linha = separando_linha[:-1]
    lista_postos = separando_linha.split(';')
    if lista_postos != ['']:
	    lista_dados.append(lista_postos)
#print(lista_dados)

for element in lista_dados:
    if element[7] not in lista_combustiveis:
        lista_combustiveis.append(element[7])

#print(lista_combustiveis)


for combustivel in lista_combustiveis:
    for element in lista_dados:
        if combustivel == element[7]:
            print(element)