import os
os.system('clear')

analisar = open('nubank.ofx', 'r')

parcelado = open('parcelado.txt', 'w')

for linha in analisar:
    if '<TRNAMT>' in linha:
        valor = (linha[8:-1])

    if '<MEMO>' in linha and '/' in linha:
        parcelas = linha[6:-1] + ':' + valor + '\n'
        parcelado.write(parcelas) 

parcelado.close()

analisar.close()