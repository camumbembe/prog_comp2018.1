from os import system
system('cls')

lista_dados = []
lista_combustiveis = []
gasolina = []
separando_linha = 'a'
preco = 0
postos = 0

preco_combustiveis = open('listaprecos.csv', 'r')

arquivopostos = open('mediapostos.txt', 'w')

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
    postos = 0
    preco = 0
    for element in lista_dados:
        if combustivel == element[7]:
            preconovo = element[8].replace(',', '.')
            preco = preco + float(preconovo)
            postos += 1
            media = preco / postos
            media = round(media, 2)
        
    print('Combustível: {:19}Preço médio: {:10}Qtd de postos: {:9}'.format(combustivel, str(media), str(postos)))
    resultado = 'Combustível: {:19}Preço médio: {:10}Qtd de postos: {:9}\n'.format(combustivel, str(media), str(postos))    
    arquivopostos.write(resultado)

preco_combustiveis.close()
arquivopostos.close()