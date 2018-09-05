print('Que triângulo é esse? Insira os ângulos do triângulo para saber seu tipo.')

lado_a = float(input('Informe o primeiro ângulo: '))
lado_b = float(input('Informe o segundo ângulo: '))
lado_c = float(input('Informe o terceiro ângulo: '))

if (lado_a < 90 ) and  (lado_b < 90) and (lado_c < 90):
  print('Esse é um triângulo acutângulo')
elif (lado_a == 90) or (lado_b == 90) or (lado_c == 90) :
  print('Esse é um triângulo retângulo')
elif (lado_a > 90) or  (lado_b > 90) or (lado_c > 90):
   print('Esse é um triângulo obtusângulo')
else:
  print('Fim do programa')