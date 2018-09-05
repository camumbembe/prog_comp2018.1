# apenas dizer se o ano é bissexto ou não, não precisa mais anos, só o informado, os dois últimos números do ano devem ser divisíveis por 4 para ser ano bissexto, ver dica questão 3 e 4 da lista 03, todos os exercicios são cumulativos, um sempre vai servir de base para o próximo, refazer todos

ano = input('Informe um ano para saber se ele é bissexto:')


if int(ano[2]) and int(ano[3]) != 0:
  if int(ano[2]) % 4 == 0 and int(ano[3]) % 4 == 0:
    print(ano, 'é um ano bissexto')
  else:
    print(ano, 'não é um ano bissexto')
else:
  if int(ano) % 4 ==0:
    print(ano,'é um ano bissexto') 
  else:
    print(ano, 'não é um ano bissexto')




