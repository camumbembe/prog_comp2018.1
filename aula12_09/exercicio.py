

palavra = input('informe uma palavra: ')

novo = ''

for letra in palavra:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        letra = '0'
        novo = novo + letra
       
    else:
        letra = '1'
        novo = novo + letra
          
print(novo)