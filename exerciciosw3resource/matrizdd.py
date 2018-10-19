matriz = [[],[],[],[],[]]
index = 0
element = 0

while True:
    element += 1
    if len(matriz[index]) <= 5:
        matriz[index].append(element)
    if element % 5 == 0:
        index+=1    
    if index == 5:
        break

print(matriz)

