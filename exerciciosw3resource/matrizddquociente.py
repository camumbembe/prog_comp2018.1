matriz = [[],[],[],[],[]]
element = 0

while element < 25:
    matriz[element//5].append(element+1)
    element += 1


print(matriz)