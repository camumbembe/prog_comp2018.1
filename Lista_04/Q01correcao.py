print('Que triângulo é esse? Insira os ângulos do triângulo para saber seu tipo.')

lado_a = float(input('Informe o primeiro ângulo: '))
lado_b = float(input('Informe o segundo ângulo: '))
lado_c = float(input('Informe o terceiro ângulo: '))

triangulo = lado_a + lado_b + lado_c

if triangulo!= 180 or lado_a == 0 or lado_b == 0 or lado_c == 0:
  print('Não é um triângulo') #se essa condição for falsa é um triangulo nao pecisa do else, apenas dos elifs
elif (lado_a == 90 or lado_b == 90 or lado_c == 90):
  print('Esse é um triângulo retângulo')
elif (lado_a > 90 or  lado_b > 90 or lado_c > 90):
  print('Esse é um triângulo obtusângulo')
else:
  print('Esse é um triângulo acutângulo')


#é necessário satisfazer a condição de ser um triângulo para só então dizer seu tipo. 