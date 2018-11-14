import random
import os
import datetime

# Chamando o comando CLEAR para limpar o conteúdo da tela
os.system('clear')


# Quantidade de elementos da lista
n = 10000


# Lista que irá armazenar todos os valores gerados randômicamente
listaValores = []


# Gerando a lista randômicamente
print('')
print('------------------------------------------------------------------')
print('Gerando a Lista Randômicamente:')
for x in range (0,n):
   listaValores.append(random.randint(0,1000))


# Salvando a lista gerada em arquivo
arquivo = open('listaoriginal.txt','w')
for valor in listaValores:
   arquivo.write('{0}\n'.format(valor))
arquivo.close()

# Ordenando a lista
print('')
print('------------------------------------------------------------------')
print('Ordenando a Lista Gerada: ')
print('')
horaInicial = datetime.datetime.now()
print('Ordenação Iniciada às...: {0}'.format(horaInicial))


qt_iteracoes = 0
#------------------------------------------------------------------------
# Início do algoritmo de ordenação
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
    


# Final do algoritmo de ordenação
#------------------------------------------------------------------------

print('')
horaFinal= datetime.datetime.now()
print('Ordenação Finalizada às.: {0}'.format(horaFinal))
print('')
tempoGasto = horaFinal - horaInicial
print('Tempo de Ordenação......: {0}'.format(tempoGasto))
print('')
print('Quantidade de Iterações.: {0}'.format(qt_iteracoes))
print('------------------------------------------------------------------')


# Salvando a lista ordenada em arquivo
arquivo = open('listaordenada.txt','w')
for valor in listaValores:
   arquivo.write('{0}\n'.format(valor))
arquivo.close()