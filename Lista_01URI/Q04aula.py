#criar um código que leia 5 números e diga o maior deles
a = int(input('Insira um valor para A:'))
b = int(input('Insira um valor para B:'))
c = int(input('Insira um valor para C:')) 
d = int(input('Insira um valor para D:')) 
e = int(input('Insira um valor para E:'))


if a > b and a > c and a > d and a > e:
  print(a, 'é o maior número')
elif b > a and b > c and b > d and b > e:
  print(b, 'é o maior número')
elif c > a and c > b and c > d and c > e:
  print(c, 'é o maior número')
elif d > a and d > b and d > c and d > e:
  print(d, 'é o maior número')
else:
  print(e, 'é o maior número')