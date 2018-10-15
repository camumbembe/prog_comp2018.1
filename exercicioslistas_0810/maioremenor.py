a = [1,3,5,7,9,11]

maior = menor = a[0]

for element in a:
    if element > maior:
        maior = element
    if element < menor:
        menor = element
print(maior, menor)