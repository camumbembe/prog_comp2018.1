from os import system
import random
system('clear')
qt_iteracoes = []

def quickSort(lista,primeiro,ultimo,contador):
   if primeiro < ultimo:
       divisor = dividir_e_organizar(lista, primeiro, ultimo, contador)


       quickSort(lista, primeiro, divisor - 1, contador)
       quickSort(lista, divisor + 1, ultimo, contador)
       

def dividir_e_organizar(lista, primeiro, ultimo, contador):
    qt_iteracoes = contador
    divisorEncontrado = False
    direcao_analise = 'pela_direita'
    pivot = primeiro
    esquerda = primeiro
    direita = ultimo
    while not divisorEncontrado:
        if (direcao_analise == 'pela_direita') :
            if lista[pivot] > lista[direita]:
                lista[pivot], lista[direita] = lista[direita], lista[pivot]
                contador.append(1)
                pivot = direita
                direcao_analise = 'pela_esquerda'
            else:
                direita = direita -1
        elif (direcao_analise == 'pela_esquerda'):
            if lista[pivot] < lista[esquerda]:
                lista[pivot], lista[esquerda] = lista[esquerda], lista[pivot]
                contador.append(1)
                pivot = esquerda
                direcao_analise = 'pela_direita'
            else:        
                esquerda = esquerda + 1
        if esquerda == direita:
            divisorEncontrado = True
    return esquerda

listaValores = []
for element in range(0, 100):	
	listaValores.append(random.randint(0, 300))
    
    
quickSort(listaValores, 0, (len(listaValores) - 1), qt_iteracoes)
print('Quantidade: ',len(qt_iteracoes))