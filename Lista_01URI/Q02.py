
a, b  = map(int,input('Enter values for A and B, separeted by comma:').split(','))


if a > b:
  if a % b == 0:
    print(a,'e', b, 'Are multiples')
  else:
    print(a,'e', b, 'Aren´t multiples')

elif a == b:
   print(a,'e', b, 'Are multiples')

else:
   if b % a == 0:
     print(a,'e', b, 'Are multiples')
   else:
      print(a,'e', b, 'Aren´t multiples')
