senha = input('Informe sua senha para verificação: ')

letter = 'qwertyuiopasdfghjklzxcvbnm'
number = '1234567890'
character = '!@#$%¨&*'

verificacao_letra = verificacao_numero = verificacao_caracter = verificacao_letram = verificacao_minlen = verificacao_maxlen = 0

for element in senha:

    if element in letter.upper():
       verificacao_letra += 1
       
    else:
       verificacao_letra = verificacao_letra
    
    if element in letter:
       verificacao_letram += 1
       
    else:
       verificacao_letram = verificacao_letram

    if element in number:
        verificacao_numero += 1
    else:
       verificacao_numero = verificacao_numero

    if element in character:
        verificacao_caracter += 1
    else:
       verificacao_caracter = verificacao_caracter

    if len(senha) > 6:
        verificacao_minlen += 1
    else:
       verificacao_minlen = verificacao_minlen

    if len(senha) < 16:
       verificacao_maxlen += 1
    else:
       verificacao_maxlen = verificacao_maxlen


if verificacao_letra > 0 and verificacao_letram > 0:
    print('As letras são válidas')
else:
   print('Verifique as letras minúsculas e maiúsculas')

if verificacao_numero > 0:
    print('Números da senha conferem')
else:
   print('Verifique a condição número')
if verificacao_caracter > 0:
    print('Caractéres estão ok')
else:
   print('Verifique se adicionou caractéres a sua senha')

if verificacao_minlen > 0 and verificacao_maxlen > 0:
    print('Tamanho da senha ok')
else:
   print('Verifique tamanho da senha')



