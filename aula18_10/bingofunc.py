import random

lista_b = []
lista_i = []
lista_n = []
lista_g = []
lista_o = []

contador = 0

while True:
    numero_b = random.randint(1,15)
    if numero_b not in lista_b and len(lista_b) <= 5:
        lista_b.append(numero_b)
    print(lista_b)

    numero_i = random.randint(16,30)
    if numero_i not in lista_i and len(lista_i) <= 5:
        lista_i.append(numero_i)
    print(lista_i)

    numero_n = random.randint(31,45)
    if numero_n not in lista_n and len(lista_n) <= 5:
        lista_n.append(numero_n)
    print(lista_n)

    numero_g = random.randint(46,60)
    if numero_g not in lista_g and len(lista_g) <= 5:
        lista_g.append(numero_g)
    print(lista_g)	

    numero_o = random.randint(61,75)
    if numero_o not in lista_o and len(lista_o) <= 5:
        lista_o.append(numero_o)
    print(lista_o)

    if len(lista_b) ==5 and len(lista_i) == 5 and len(lista_n) == 5 and len(lista_g) == 5 and len(lista_o) == 5:
        break

print(lista_b)
print(lista_i)
print(lista_n)
print(lista_g)
print(lista_o)

