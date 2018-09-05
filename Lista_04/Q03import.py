from math import sqrt
print('Vamos encontrar as raízes da equação')

a = int(input('Informe o valor de A: '))
b = int(input('Informe o valor de B: '))
c = int(input('Informe o valor de C: '))

delta = (b **2) - (4 * a * c)

x_1 = ((-b) + (sqrt(delta))) / (2 * a)

x_2 = ((-b) - (sqrt(delta))) / (2 * a)

print('As raízes da equação são:', x_1, 'e', x_2)