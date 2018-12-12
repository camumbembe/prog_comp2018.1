import os

os.system('cls')

def media_notas(nota_1, nota_2, nota_3, nota_4):
    media = (float(nota_1) + float(nota_2) + float(nota_3) + float(nota_4)) / 4
    return round(media,1)

def situacao(media):
    if media >= 5:
        return 'Aprovado'
    else:
        return 'Reprovado'

def str_cpf(cpf):
    string_cpf = cpf[:3]+ '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:12]
    return string_cpf

try:
	analisar = open('dados_alunos.txt', 'r')
	
except FileNotFoundError:
    print('Arquivo não existe.')
    criar = open('dados_alunos.txt', 'w')

    while True:
        try:
            cpf = int(input('Informe os números do CPF: '))
        except ValueError:
            print('O CPF deve ser composto apenas de números.')
            continue
        else:
            if int(cpf) == 0:
                break
            if len(str(cpf)) != 11:
                print('Digite um CPF válido, 11 dígitos')
                continue
            nome = input('Informe o nome do aluno: ')
            while True:
                try:
                    nota1 = float(input('Informe a primeira nota do aluno: '))
                    nota2 = float(input('Informe a segunda nota do aluno: '))
                    nota3 = float(input('Informe a terceira nota do aluno: '))
                    nota4 = float(input('Informe a quarta nota do aluno: '))
                except ValueError:
                    print('As notas devem ser compostas por números inteiros e/ou decimais.')
                    continue
                else:
                    if nota1 < 0 or nota2 < 0 or nota3 < 0 or nota4 < 0:
                        print('As notas devem ser compostas por números positivos.')
                        continue
                    break

        texto_arquivo = str(cpf) + ';' + nome + ';' + str(nota1) + ';' + str(nota2) + ';' + str(nota3) +  ';' + str(nota4) + '\n'			
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
    for aluno in dici_tuple:
        media_aluno = media_notas(aluno[1][1], aluno[1][2], aluno[1][3],aluno[1][4])
        print('Nome: {:15}CPF: {:19}Média: {:7}Situação: {:5}'.format(
        aluno[1][0], 
        str_cpf(aluno[0]), 
        str(media_aluno), 
        situacao(media_aluno)
        )) 
    verificacao = input('Informe o CPF do aluno que deseja verificar: ')
    try:
        media_aluno = media_notas(dicionario[verificacao][1], dicionario[verificacao][2], dicionario[verificacao][3], dicionario[verificacao][4])
        print('\n CPF: {:19}Nome: {:10} \n Nota 1: {:5}Nota 2: {:5}Nota 3: {:5}Nota 4: {:5} \n Média: {:5}Situação: {:5}'.format(str_cpf(verificacao), 
        dicionario[verificacao][0], 
        dicionario[verificacao][1], 
        dicionario[verificacao][2], 
        dicionario[verificacao][3], 
        dicionario[verificacao][4], 
        str(media_aluno), 
        situacao(media_aluno)
        ))
    except KeyError:
        print('CPF não encontrado')

        
