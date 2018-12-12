import os
os.system('clear')

lista = []


try:
	analisar = open('dados_pessoais.txt', 'r')
	
    
except FileNotFoundError:
    print('Arquivo não existe.')
    criar = open('dados_pessoais.txt', 'w')

    while True:
        cpf = input('Informe os números do CPF: ')
        if int(cpf) == 0:
            break
        if len(cpf) != 11:
            print('Digite um CPF válido, 11 dígitos')
            continue
        nome = input('Informe o nome: ')
        cidade = input('Informe a cidade: ')
        devendo = input('Informe o valor da dívida: ')
        pago = input('Informe quanto foi pago: ')
		
	
		
        texto_arquivo = str(cpf) + '-' + nome + '-' + cidade + '-' + devendo + '-' + pago +'\n'			
        criar.write(texto_arquivo)

    criar.close()
    
else:
    for linha in analisar:
        if  '\n' in linha:
            dados = linha[:-1].split('-')
            
        else:
            dados = linha.split('-')
            
        dados[0], dados[1] = dados[1], dados[0]	
        lista.append(dados)
        
    lista.sort()

    for pessoa in lista:        
        string_cpf = pessoa[1][:3]+ '.' + pessoa[1][3:6] + '.' + pessoa[1][6:9] + '-' + pessoa[1][9:12]
        diferenca = int(pessoa[3]) - int(pessoa[4])
        print('Nome: {:20}Cidade: {:15}CPF: {:19}Devendo: {:9}Pago: {:5}Diferença: {:5} '.format(pessoa[0], pessoa[2], string_cpf, pessoa[3], pessoa[4], diferenca) ) 
	
analisar.close()