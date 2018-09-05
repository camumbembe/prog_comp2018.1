RedimentoBruto = float(input('Informe seu rendimento bruto acumulado durante o ano:'))

print('')

ImpostoFonte = float(input('Informe o imposto retido na fonte:'))

print('')

PrevidenciaOficial = float(input('Informe sua contribuição previdenciária oficial:'))

print('')

QtDependentes = float(input('Quantas pessoas são seus dependentes?:'))

print('')

MesesDpdt = float(input('Por quanto meses eles são seus dependentes?:'))

print('')

Pensao = float(input('Informe o valor pago de pensão alimentícia: '))

print('')

OutrasDeducoes = float(input('Informe a soma de outras deduções: '))

print('')

BaseCalculo = RedimentoBruto - ImpostoFonte - PrevidenciaOficial - (QtDependentes * 189.59 * MesesDpdt) - Pensao - OutrasDeducoes



print('A base para o cálculo do seu imposto é:', BaseCalculo)

if BaseCalculo <= 1903.98:
  print('Você está isento do imposto de renda.')
elif ((BaseCalculo > 1903.99) and (BaseCalculo <= 2826.65)):
  ImpostoFaixa = BaseCalculo * 0.075
  print('Seu Imposto de Renda é R$', ImpostoFaixa)
elif ((BaseCalculo >= 2826.66) and (BaseCalculo <= 3751.05)):
  ImpostoFaixa = BaseCalculo * 0.15
  print('Seu Imposto de Renda é R$', ImpostoFaixa)
elif ((BaseCalculo >= 3751.06) and (BaseCalculo <= 4664.68)):
  ImpostoFaixa = BaseCalculo * 0.225
  print('Seu Imposto de Renda é R$', ImpostoFaixa)
else:
  ImpostoFaixa = BaseCalculo * 0.275
  print('Seu Imposto de Renda é R$', ImpostoFaixa)
