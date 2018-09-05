print('Que triângulo é esse? Insira os lados do triângulo para saber seu tipo.')

lado_a = float(input('Informe o primeiro lado: '))

lado_b = float(input('Informe o segundo lado: '))

lado_c = float(input('Informe o terceiro lado: '))



if (lado_a <= 0) or (lado_b <= 0)  or (lado_c <= 0):
  print('Não pode haver lado igual ou inferior a zero')
elif (lado_a >= lado_b + lado_c) or (lado_b >= lado_a + lado_c) or (lado_c >= lado_b + lado_a):
  print('Os lados informados não formam um triângulo')
elif (lado_a == lado_b) and (lado_c == lado_b):
  print('O triângulo é equilátero')
elif (lado_a == lado_b) or (lado_b == lado_c) or (lado_c == lado_a):
  print('O triângulo é isóceles')
else:
  print('O triângulo é escaleno')