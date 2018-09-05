print('Vamos encontrar as raízes da equação')

a = float(input('Informe o valor de A: '))
b = float(input('Informe o valor de B: '))
c = float(input('Informe o valor de C: '))


if a == 0:
  print('Não é possivel calcular as raízes da equação')
else:
   delta = (b **2) - (4 * a * c)
   if (delta > 0):
      x_1 = ((-b) + (delta **(1/2))) / (2 * a)
      x_2 = ((-b) -(delta **(1/2))) / (2 * a)
      print('As raízes são reais, x1=', x_1, 'e x2=', x_2)
   elif (delta == 0):
      x_1 = (-b) / (2 * a)
      print('As raízes da equação são iguais, x1 e x2 =', x_1)
   else:
      print('Essa equação não possui raiz real.')