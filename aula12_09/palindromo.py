
palavra = input('Entre com uma palavra para descobrir se é um palíndromo: ')

palindromo = ''

for letra in palavra:
    palindromo = letra + palindromo
if palavra == palindromo:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')


