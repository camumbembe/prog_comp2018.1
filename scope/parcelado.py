analisar = open('nubank.ofx', 'r')

parcelado = open('parcelado.txt', 'w')

for linha in analisar:
    if '<TRNAMT>' in linha:
        valor = (linha[8:])
    if ('<MEMO>' and '/') in linha:
        parcelado = linha[6:] + ':' + valor
        linhas.write(parcelado) 

parcelado.close()

analisar.close()