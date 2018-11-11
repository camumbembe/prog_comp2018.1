import random

lista = [4,8,3,9,12,1,5]

pivot = ''
direita =  lista[len(lista)//2:]
esquerda = lista[:len(lista)//2]


print(pivot)
print(direita)
print(esquerda)


for element in lista:
    pivot = (random.choice(lista))
    if pivot in direita:
        if element < pivot:
            lista[element], lista[pivot] = lista[pivot], lista[element]  
            print(lista)
        if pivot in esquerda:
            if element > pivot:
                lista[element], lista[pivot] = lista[pivot], lista[element]  
            print(lista)
