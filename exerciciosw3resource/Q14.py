palavra = input('Informe uma palavra e vamos calcular suas letras e digitos: ')

letras = 'qwertyuiopasdfghjklçzxcvbnm'
digitos = '1234567890'

quantidade_letras = 0
quantidade_digitos = 0

for element in palavra:
    if element in letras:
        quantidade_letras += 1
    elif element in digitos:
        quantidade_digitos += 1

print('A quantidade de letras em {0} é {1} e de dígitos é {2}'.format(palavra, quantidade_letras, quantidade_digitos))        