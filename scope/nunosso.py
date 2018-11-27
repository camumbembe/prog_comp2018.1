analisar = open('nubank.ofx', 'r')

linhas = open('linhas.txt', 'w')

for linha in analisar:
    if '<TRNAMT>' in linha:
        valor = (linha[8:])
    if '<MEMO>' in linha:
        resultado = linha[6:] + ':' + valor 
        linhas.write(resultado) 
            
linhas.close()


analisar.close()


# linhas = open('linhas.txt', 'w')


# for linha in analisar:
#     if '<MEMO>'  in linha:
#         linhas.write(linha[6:])
            
    

# linhas.close()
