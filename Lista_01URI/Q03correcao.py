
import sys

ano = int(input('Informe o ano: '))

if (ano < 1000) or (ano > 9999): 
  print('Ano Inválido !!!!!')
  sys.exit()

ano = ano % 1000
ano = ano % 100

if (ano % 4 == 0):
  print('Ano Bissexto!!!!')
else:
  print('O Ano NÃO é Bissexto')


  #resposta 2

  import sys

ano = int(input('Informe o ano: '))

if (ano < 1000) or (ano > 9999): 
  print('Ano Inválido !!!!!')
  sys.exit()

ano_auxiliar = ano % 1000
ano_auxiliar = ano_auxiliar % 100

print(ano_auxiliar)

if (ano % 4 == 0):
  print('O Ano {0} é Bissexto!!!!!'.format(ano))
else:
  print('O Ano {0} NÃO é Bissexto!!!!!'.format(ano))


#resolção 3

'''
Verificando se o ano é BISSEXTO
'''

import sys

ano = int(input('Informe o ano: '))

if ano < 1000 or ano > 9999:
  print('Informe um valor entre 1000 e 9999')
  sys.exit()

ano_auxiliar = ano
ano_auxiliar = ano_auxiliar % 1000
ano_auxiliar = ano_auxiliar % 100

if ano % 4 == 0:
  print('O ano {0} é BISSEXTO'.format(ano))
else:
  print('O ano {0} NÃO é BISSEXTO'.format(ano))
