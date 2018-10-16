
listaValores = [None, None, None, None, None]

while True:
    valor = int(input('Informe um valor: '))
    listaValores.append(valor)
    listaValores.pop(0)
    if (valor == 0):
        break
    print(listaValores)

