def makinglist(numbername, listname, lenlist):
    if numbername not in listname and lenlist <= 5:
        listname.append(numbername)
        
import random

lista_b = []
lista_i = []
lista_n = []
lista_g = []
lista_o = []

contador = 0

while True:
        numero_b = random.randint(1,15)
        makinglist(numero_b, lista_b, len(lista_b))  

        numero_i = random.randint(16,30)
        makinglist(numero_i, lista_i, len(lista_i))

        numero_n = random.randint(31,45)
        makinglist(numero_n, lista_n, len(lista_n))

        numero_g = random.randint(46,60)
        makinglist(numero_g, lista_g, len(lista_g))

        numero_o = random.randint(61,75)
        makinglist(numero_o, lista_o, len(lista_o))


        if len(lista_b) ==5 and len(lista_i) == 5 and len(lista_n) == 5 and len(lista_g) == 5 and len(lista_o) == 5:
                break

print(lista_b)
print(lista_i)
print(lista_n)
print(lista_g)
print(lista_o)
