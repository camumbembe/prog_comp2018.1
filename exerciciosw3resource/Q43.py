numero = int(input('Informe um número pra ver sua tabuada de multiplicação: '))

for element in range(0, 11):
    result = numero * element
    print('{0} x {1} = {2}'.format(numero, element,result))