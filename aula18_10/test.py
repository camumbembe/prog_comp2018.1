import random
from os import system 

system('clear')

arquivo = open('cartela.txt', 'w')

lista_bingo = []
number = None

def makinglist(inicial, final):
	lista = []
	while True:
		number = random.randint(inicial, final)
		if (number not in lista) and (len(lista) <= 5):
			lista.append(number)
		if (len(lista) == 5):
			lista.sort()
			lista_bingo.append(lista)
			break			
	# return lista


makinglist(1, 15)  
makinglist(16,30)
makinglist(31,45)
makinglist(46,60)
makinglist(61,75)

contador = 0

print(" +-----+-----+-----+-----+-----+ \n |  B  |  I  |  N  |  G  |  O  | \n +-----+-----+-----+-----+-----+ ")
while (contador < 5):
	print(" |", end ='')
	for listas in lista_bingo:
		print(" {num:02d}".format(num= listas[contador]), end="  |")
	contador+= 1

	print("\n +-----+-----+-----+-----+-----+")



