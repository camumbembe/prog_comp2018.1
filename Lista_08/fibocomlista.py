quantidade = int(input('Informe quantos números da sequência de fibonacci você deseja conhecer: '))

penultimo = 0
ultimo = 1

listafibo = []

for elemento in range(1, quantidade+1):
    proximo = penultimo + ultimo
    penultimo = ultimo
    ultimo = proximo
    listafibo.append(penultimo)

print('A sequencia de fibonacci com {0} números é: {1}'.format(quantidade,listafibo))