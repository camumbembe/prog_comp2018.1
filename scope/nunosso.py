import os
os.system('clear')

analisar = open('nubank.ofx', 'r')

linhas = open('linhas.txt', 'w')
parcelado = open('parcelado.txt', 'w')

total = 0

for linha in analisar:
    if '<TRNAMT>' in linha:
        valor = (linha[8:-1]) #remover o negativo (como fazer com os créditos?)
        valor = float(valor) * (-1)

    if '<MEMO>' in linha and '/' not in linha and 'Pagamento recebido' not in linha:
        resultado = linha[6:-1] + ' ' + str(valor) + '\n'
        total = total + float(valor)
        linhas.write(resultado)
 

    elif '<MEMO>' in linha and '/' in linha:
        barra = linha.find('/')
               
        if linha[barra-2] == '':
            pqt = linha[barra -1]

        else:
            pqt = linha[barra-2:barra]

        if linha[barra+2] == '':
            qpf = linha[barra +1]

        else:
            qpf = linha[barra+1:barra+3]
        
        r_parcelas = int(qpf) - int(pqt)
        t_parcelas = r_parcelas * valor
     
        parcelas = linha[6:-1] + '  ' + str(valor) + ' ' +  str(t_parcelas) + '\n'
        total = total + float(valor)
        parcelado.write(parcelas) 

    




parcelado.close()     
    
linhas.close()

analisar.close()


# linhas = open('linhas.txt', 'w')


# for linha in analisar:
#     if '<MEMO>'  in linha:
#         linhas.write(linha[6:])
            
    

# linhas.close()
