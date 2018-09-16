SalarioBruto = float(input('Informe seu salário bruto: '))

Contribuição = SalarioBruto - 0.1

Imposto = SalarioBruto - 0.05

SalarioLiquido = (Contribuição + Imposto) - SalarioBruto

print('Após descontos, seu salário de R${0}, passa a ser de R${1}'.format(SalarioBruto, SalarioLiquido))
