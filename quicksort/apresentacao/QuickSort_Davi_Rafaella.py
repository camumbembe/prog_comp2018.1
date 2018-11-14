
listaValores = [4, 1, 2, 5, 3, 7, 6, 5]
contador = 0   

def quickSort(lista,primeiro,ultimo):
   if primeiro < ultimo:
        #chama a função "dividir_e_organizar" e atribui o retorno dela à variavel "divisor"
       divisor = dividir_e_organizar(lista, primeiro, ultimo)

        #Chama novamente a função quickSort, criando novos frames( esquerda e direita), com os seguintes argumentos:
       quickSort(lista, primeiro, divisor - 1)
       quickSort(lista, divisor + 1, ultimo)
       

def dividir_e_organizar(lista, primeiro, ultimo):
    global contador
    divisorEncontrado = False
    direcao_analise = 'pela_direita'
    pivot = primeiro
    esquerda = primeiro
    direita = ultimo
    while not divisorEncontrado:
        if (direcao_analise == 'pela_direita') :
            if lista[pivot] > lista[direita]:
                lista[pivot], lista[direita] = lista[direita], lista[pivot]
                contador += 1
                pivot = direita
                direcao_analise = 'pela_esquerda'
            else:
                direita = direita -1
        elif (direcao_analise == 'pela_esquerda'):
            if lista[pivot] < lista[esquerda]:
                lista[pivot], lista[esquerda] = lista[esquerda], lista[pivot]
                contador += 1
                pivot = esquerda
                direcao_analise = 'pela_direita'
            else:        
                esquerda = esquerda + 1
        if esquerda == direita:
            divisorEncontrado = True
    return esquerda

quickSort(listaValores, 0, (len(listaValores) - 1))
qt_iteracoes = contador

print(listaValores, qt_iteracoes)