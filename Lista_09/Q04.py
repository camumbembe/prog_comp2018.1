
import random
import statistics

n = int(input('Informe o valor de n: '))
lista_n = []

for element in range(0, n):	
	lista_n.append(random.randint(0,99))

print('Lista gerada: ',lista_n)

print('Media dos valores : {0}'.format(statistics.mean(lista_n))) 
#procurar a biblioteca e suas funções para fazer essa questão



	
