import random

lista_b = []
lista_i = []
lista_n = []
lista_g = []
lista_o = []

#estudar conceito de funcao e como criar uma funcao em python
contador = 0

while contador < 5:
	numero_b = random.randint(1,15)
	if numero_b not in lista_b:
		lista_b.append(numero_b)
		contador +=1
contador = 0
while contador < 5:
	numero_i = random.randint(16,30)
	if numero_i not in lista_i:
		lista_i.append(numero_i)
		contador +=1
contador = 0
while contador < 5:
	numero_n = random.randint(31,45)
	if numero_n not in lista_n:
		lista_n.append(numero_n)
		contador +=1	
contador = 0
while contador < 5:
	numero_g = random.randint(46,60)
	if numero_g not in lista_g:
		lista_g.append(numero_g)
		contador +=1
contador = 0
while contador < 5:
	numero_o = random.randint(61,75)
	if numero_o not in lista_o:
		lista_o.append(numero_o)
		contador +=1

print(lista_b, lista_i, lista_n, lista_g, lista_o)

# print(lista_b)
# print(lista_i)
# print(lista_n)
# print(lista_g)
# print(lista_o)

# and len(lista_n) and len(lista_g) and len(lista_o)