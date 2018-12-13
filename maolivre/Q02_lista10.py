from os import system
system('cls')
lista_dados = []

def imprimenome(nomedoarquivo):
    nomes = 'a'
    while nomes:
        nomes = nomedoarquivo.readline()
        if  '\n' in nomes:
            nomes = nomes[:-1]
        lista_nomes = nomes.split('#')
        if lista_nomes != ['']:
            lista_nomes[0], lista_nomes[1] = lista_nomes[1], lista_nomes[0]
            lista_dados.append(lista_nomes)
    nomedoarquivo.close()    
    lista_dados.sort()
    
    for dados in lista_dados:
        orgCpf = (dados[1][:3]) + '.' + (dados[1][3:6]) + '.' + (dados[1][6:9]) + '-' + (dados[1][9:12])
        print('Nome: {:15}Cidade: {:15}CPF: {:10}'.format((dados[0]), (dados[2]), orgCpf))
    
    verificacao = input('Informe um CPF para acessar seus dados: ')
    for pessoa in lista_dados:
       if pessoa[1] == verificacao:
           org_Cpf = (pessoa[1][:3]) + '.' + (pessoa[1][3:6]) + '.' + (pessoa[1][6:9]) + '-' + (pessoa[1][9:12])
           print('CPF: {:10}\nNome: {:10}\nCidade: {:10}'.format(org_Cpf, pessoa[0], pessoa[2]))



try:
    arquivoSupers = open('dadospessoais.1.txt', 'r')

except FileNotFoundError:
    arquivoNovo = open('dadospessoais.1.txt', 'w')
    while True:
        try:
            cpf_pessoa = input('Informe o CPF: ')
            int(cpf_pessoa)
        except ValueError:
            print('Informe um número inteiro')
            continue
        else:             
            if int(cpf_pessoa) == 0:
                break
            if len(str(cpf_pessoa)) != 11:
                print('Informe um CPF válido - 11 dígitos.')
                continue
            nome_pessoa = input('Informe o nome a ser adicionado a lista: ').title()
            cidade_pessoa = input('Informe a cidade: ')
            conteudo = str(cpf_pessoa) + '#' + nome_pessoa + '#' + cidade_pessoa + '\n'
            arquivoNovo.write(conteudo)
    arquivoNovo.close()
    arquivoSupers = open('dadospessoais.1.txt', 'r')
    imprimenome(arquivoSupers)



else:
    imprimenome(arquivoSupers)


    

