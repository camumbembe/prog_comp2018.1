
listaValores = ['null', 'null', 'null', 'null', 'null']

while True:
    valor = int(input('Informe um valor: '))
    listaValores.append(valor)
    if len(listaValores) > 5:
        listaValores.pop(0)
    if (valor == 0):
        break
    print(listaValores)