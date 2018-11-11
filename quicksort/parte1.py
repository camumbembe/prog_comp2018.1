from os import system
system('cls')
import random

n = int(input('Informe o valor de n: '))

lista_n = []
for element in range(0, n):	
	lista_n.append(random.randint(0,9))

print(lista_n)

pivot = 7
esquerda = 0
direita = len(lista_n) - 1

 #while aqui para repetir enquanto a esquerda for < que a len(lista_n) (e a direita?)!=0 ?

 
if pivot > (len(lista_n) //  2):
    if lista_n[pivot] < lista_n[esquerda]:
        lista_n[pivot], lista_n[esquerda] = lista_n[esquerda], lista_n[pivot]  
        print(lista_n)
                       
    else:        
        esquerda = esquerda + 1

elif pivot < (len(lista_n) //  2):
    if lista_n[pivot] > lista_n[direita]:
        lista_n[pivot], lista_n[direita] = lista_n[direita], lista_n[pivot]
        print(lista_n)
    else:
        direita = direita -1
else:
    print()
    #pode ir para qualquer lado? 









