import os

os.system('cls')

lista = []


try:
	analisar = open('dados_alunos.txt', 'r')
	
    
except FileNotFoundError:
	print('Arquivo não existe.')
	criar = open('dados_alunos.txt', 'w')
	
	while True:
		cpf = input('Informe os números do CPF: ')
		if int(cpf) == 0:
			break
		if len(cpf) != 11:
			print('Digite um CPF válido, 11 dígitos')
			continue

		nome = input('Informe o nome do aluno: ')
		notas = input('Informe as notas do aluno: ')
		
	
		
		texto_arquivo = str(cpf) + '#' + nome + '#' + notas + '\n'			
		criar.write(texto_arquivo)


	criar.close()	
else:
    dicionario = {}
    for linha in analisar:
        if  '\n' in linha:
            dados = linha[:-1].split(';')
        else:
            dados = linha.split(';')
        if len(dados) > 1:
            
            #media_notas
            media_notas = ( 
            float(dados[2]) + 
            float(dados[3]) + 
            float(dados[4]) + 
            float(dados[5]) 
            ) / 4	
            dicionario[dados[0]] = [dados[1], dados[2],dados[3],dados[4],dados[5], media_notas]      


	
    analisar.close()
dici_tuple = sorted(dicionario.items(), key= lambda x: x[1])        

def situacao(media):
    if media >= 5:
        return 'Aprovado'
    else:
        return 'Reprovado'



for aluno in dici_tuple:
    #string_cpf = pessoa[1][:3]+ '.' + pessoa[1][3:6] + '.' + pessoa[1][6:9] + '-' + pessoa[1][9:12]
    print('Nome: {:15}CPF: {:25}Média: {:20}Situação: {:5}'.format(aluno[1][0], aluno[0], aluno[1][5], situacao(aluno[1][5]))) 
    
# verificacao = input('Informe o CPF do aluno que deseja verificar: ')

