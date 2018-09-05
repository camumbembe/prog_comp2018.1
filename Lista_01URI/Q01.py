from numpy import random

N = int(input('Informe um número positivo, menor que 10000:'))

while ((N <= 0) or (N > 10000)): 
  N = int(input('Informe um número positivo, menor que 10000:'))

numbers = random.randint(-10**7, 10**7, size=N)

print(numbers)

for i in numbers:
  if i % 2 == 0 and i > 0:
    print(i,'EVEN POSITIVE')
  elif i % 2 == 0 and i < 0:
    print(i, 'EVEN NEGATIVE')
  elif i % 2 != 0 and i > 0:
    print(i, 'ODD POSITIVE')
  elif i % 2 != 0 and i < 0:
    print(i, 'ODD NEGATIVE')
  else:
    print(i, 'NULL')
  