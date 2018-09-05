
a = int(input('Informe um valor para A:'))
b = int(input('Informe um valor para B:'))

if a > b:
  if a % b == 0:
    print(a,'e', b, 'São múltiplos')
  else:
    print(a,'e', b, 'Não são múltiplos')

elif a == b:
   print(a,'e', b, 'São múltiplos')

else:
   if b % a == 0:
     print(a,'e', b, 'São múltiplos')
   else:
      print(a,'e', b, 'Não são múltiplos')