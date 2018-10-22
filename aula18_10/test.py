def makinglist(numbername, listname, lenlist):
    if numbername not in listname and lenlist <= 5:
        listname.append(numbername)
        print(listname)



import random

lista_b = []
lista_i = []
lista_n = []
lista_g = []
lista_o = []

contador = 0

while True:
    numero_b = random.randint(1,15)
    makinglist(numero_b, lista_b,len(lista_b)   

    if len(lista_b) == 5:
        break