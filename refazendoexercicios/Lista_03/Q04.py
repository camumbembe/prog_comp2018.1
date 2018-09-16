numero = int(input('Informe um número de três algarismos: '))

centena = numero // 100
numero = numero % 100

dezena = numero // 10
numero = numero % 10

unidade = numero

print('O inverso do número é ', unidade, dezena, centena)