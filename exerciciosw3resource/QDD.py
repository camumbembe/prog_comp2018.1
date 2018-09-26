nome = input('Informe seu nome e sobrenome: ')
palavra =  ''



for element in nome:
    if element != ' ':
        palavra =  palavra + element
    else:
        nome =  palavra
        palavra = ''
    
print('{0},{1}'.format(palavra, nome))
    