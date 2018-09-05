a = int(input('Insira um valor para A:'))
b = int(input('Insira um valor para B:'))
c = int(input('Insira um valor para C:')) 
d = int(input('Insira um valor para D:')) 
e = int(input('Insira um valor para E:'))

maior_numero = ''

if a >= b and a >= c and a >= d and a >= e:
  maior_numero = 'A'
  resultado = a
  
if b >= a and b >= c and b >= d and b >= e:
  maior_numero = maior_numero + ' ' +'B'
  resultado = b

if c >= a and c >= b and c >= d and c >= e:
  maior_numero = maior_numero + ' ' + 'C'
  resultado = c

if d >= a and d >= b and d >= c and d >= e:
  maior_numero = maior_numero + ' ' + 'D'
  resultado = d
  
  
if e >= a and e >= b and e >= c and e >= d :
  maior_numero = maior_numero + ' ' +'E'
  resultado = e
  
print('Maior número:',resultado, maior_numero)