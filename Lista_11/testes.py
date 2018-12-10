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
            dicionario[dados[0]] = [dados[1], dados[2],dados[3],dados[4],dados[5]]      

    analisar.close()


dici_tuple = sorted(dicionario.items(), key= lambda x: x[1])        

def media_notas(nota_1, nota_2, nota_3, nota_4):
    media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
    return round(media,2)


def situacao(media):
    if media >= 5:
        return 'Aprovado'
    else:
        return 'Reprovado'



for aluno in dici_tuple:
    #string_cpf = pessoa[1][:3]+ '.' + pessoa[1][3:6] + '.' + pessoa[1][6:9] + '-' + pessoa[1][9:12]
    print('Nome: {:15}CPF: {:25}Média: {:20}Situação: {:5}'.format(aluno[1][0], aluno[0], aluno[1][5], situacao(aluno[1][5]))) 
    
# verificacao = input('Informe o CPF do aluno que deseja verificar: ')

