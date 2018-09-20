temperatura = input('Informe a temperatura a ser convertida com a unidade no fim: ')

letrasc = 'Cc'
letrasf = 'Ff'

graus = ''

for elemento in temperatura:
    if elemento not in letrasc and elemento not in letrasf:
        graus =  graus + elemento 
    elif elemento in letrasc:
        c = f = float(graus)
        fahrenheit = (160 + 9 * c)/5
        print('A temperatura {0} em fahrenheit é {1}F'.format(temperatura, fahrenheit))
    else:
        c = f = float(graus)
        celsius = (5 * f - 160)/9
        print('A temperatura {0} em celsius é {1}C'.format(temperatura, celsius))
        



