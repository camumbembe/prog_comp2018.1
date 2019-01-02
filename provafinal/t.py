lista = [['davi', 'imprime', 27], ['caetano', 'agua', 34], [
    'rafa', 'thcuin', 52], ['caetano', 'tia', 45], ['rafa', 'bunda seca', 12], ['bela', 'davi', 48], ['davi', 'sou chato mesmo', 54]]
pessoas = ['caetano', 'davi', 'rafa']

for nome in pessoas:
    for minilista in lista:
        if nome in minilista[0]:
            print(minilista)

print('acabou o programa')