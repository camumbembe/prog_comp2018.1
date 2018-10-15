user_input = int(input('Insert a number:'))
lista_primos = [2]
verificador = 2
contador = ''


while user_input % verificador != 0:
    verificador = verificador + 1 
    contador = True

    if verificador == user_input:
        break
    if  user_input % verificador == 0:
        contador = False
        print('is is not prime number')
        
if contador == True:
    print('it is a prime number')


    
