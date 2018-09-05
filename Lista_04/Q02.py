print('Que triângulo é esse? Insira os lados do triângulo para saber seu tipo.')

lado_a = float(input('Informe o primeiro lado: '))
lado_b = float(input('Informe o segundo lado: '))
lado_c = float(input('Informe o terceiro lado: '))

if (lado_a == lado_b) and (lado_c == lado_b):
  print('Esse é um triângulo equilátero')
elif (lado_a == lado_b) or (lado_b == lado_c) or (lado_c == lado_a) :
  print('Esse é um triângulo isóceles')
elif (lado_a != lado_b) and (lado_b != lado_c) and (lado_c != lado_a):
   print('Esse é um triângulo escaleno')
else:
  print('Fim do programa')