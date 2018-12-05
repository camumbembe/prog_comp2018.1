import os
os.system('clear')

lista = []


try:
	analisar = open('dados_pessoais.txt', 'r')
	linha = 'a'
	while linha:
		linha = analisar.readline()

		if  '\n' in linha:
			dados = linha[:-1].split('#')
			
		else:
			dados = linha.split('#')
		
		if len(dados) > 0:
			dados[0], dados[1] = dados[1], dados[0]	
			lista.append(dados)
		
	lista.sort()
	
	for pessoa in lista:
		print('Nome: {:20}Cidade: {:15}CPF: {:10}  '.format(pessoa[0], pessoa[2], pessoa[1]) ) 
	

	analisar.close()
	
    
except FileNotFoundError:
	print('Arquivo não existe.')
	criar = open('dadosnovos.txt', 'w')
	while True:
		cpf = int(input('Informe os números do CPF: '))
		if cpf == 0:
			break
		nome = input('Informe o nome: ')
		cidade = input('Informe a cidade: ')
		
	
		
		texto_arquivo = str(cpf) + '#' + nome + '#' + cidade + '\n'			
		criar.write(texto_arquivo)


	criar.close()	




        
	

		


