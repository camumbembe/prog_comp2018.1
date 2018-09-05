
ano = int(input('Informe um ano para saber se ele é bissexto:'))

if ano % 4 == 0 and ano % 100 != 0:
  print(ano, 'é um ano bissexto')
elif ano % 400 == 0:
  print(ano, 'é um ano bissexto')
else:
  print(ano, 'não é um ano bissexto')
