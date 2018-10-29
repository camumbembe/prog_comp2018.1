
import random
import statistics

n = int(input('Informe o valor de n: '))
lista_n = []

for element in range(0, n):	
	lista_n.append(random.randint(0,99))

print('Lista gerada: ',lista_n)

print('A media dos valores: {0}'.format(statistics.mean(lista_n))) 
print('A mediana da lista: {0}'.format(statistics.median(lista_n))) 
print('A variancia da lista: {0}'.format(statistics.pvariance(lista_n))) 
print('O desvio padrao da lista: {0}'.format(statistics.stdev(lista_n))) 
#procurar a biblioteca e suas funções para fazer essa questão



	
