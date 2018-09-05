'''
Programa para verificar qual o
maior entre 5 números digitados
'''

valor_x1 = int(input('Informe o Valor X(1): '))
maior = valor_x1

valor_x2 = int(input('Informe o Valor X(2): '))
if (valor_x2 > maior): maior = valor_x2

valor_x3 = int(input('Informe o Valor X(3): '))
if (valor_x3 > maior): maior = valor_x3

valor_x4 = int(input('Informe o Valor X(4): '))
if (valor_x4 > maior): maior = valor_x4

valor_x5 = int(input('Informe o Valor X(5): '))
if (valor_x5 > maior): maior = valor_x5

print('O maior número é {0}'.format(maior))



#resolução 2

'''
Programa para verificar qual o
maior entre 5 números digitados
'''

valor_x1 = int(input('Informe o Valor X(1): '))
valor_x2 = int(input('Informe o Valor X(2): '))
valor_x3 = int(input('Informe o Valor X(3): '))
valor_x4 = int(input('Informe o Valor X(4): '))
valor_x5 = int(input('Informe o Valor X(5): '))

maior = valor_x1

if (valor_x2 > maior): maior = valor_x2

if (valor_x3 > maior): maior = valor_x3

if (valor_x4 > maior): maior = valor_x4

if (valor_x5 > maior): maior = valor_x5

print('O maior número é {0}'.format(maior))