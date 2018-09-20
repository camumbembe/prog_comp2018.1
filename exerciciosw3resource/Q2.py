temperatura = input('Informe a temperatura a ser convertida com a unidade no fim: ')

letrasc = 'Cc'
letrasf = 'Ff'



graus = ''

for elemento in temperatura:
    if elemento in letrasc:
        unidade = 'celsius'
    elif elemento in letrasf:
        unidade = 'fahrenheit'
    else: 
        graus =  graus + elemento 

c = f = float(graus)

if unidade == 'celsius':
    fahrenheit = (160 + 9 * c)/5
    print('A temperatura {0} em fahrenheit é {1}F'.format(temperatura, fahrenheit))
else:
    celsius = (5 * f - 160)/9
    print('A temperatura {0} em celsius é {1}C'.format(temperatura, celsius))






