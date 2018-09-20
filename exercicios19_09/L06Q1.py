
#Questão 1 e 2 não podem ser feitas usando for


numeros = int(input('Informe um número: '))

itens = ''

for element in numeros:
	itens = itens + element
	maior = itens

if (itens > maior): 
	itens = maior


print('O maior número é', maior)




