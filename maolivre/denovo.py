from os import system
system('cls')

conteudo = 'a'
lista_dados = []

try:
    financeiro = open('dados_pessoais.txt', 'r')

except FileNotFoundError:
    novofinanceiro = open('dados_pessoais.txt', 'w')
    while True:
        cpf = input('Informe o CPF: ').upper()
        if str(cpf) == 'EXIT':
            break
        nome = input('Informe o nome do endividado: ')
        cidade = input('Informe o endereço: ')
        divida = input('Informe o valor da dívida: ')
        pago = input('Informe quanto da dívida já foi pago: ')
        qnt_falta = input('Informe quanto ainda resta da dívida: ')
        dados_divida = cpf + '-' + nome + '-' + cidade + '-' + divida + '-'+ pago
        novofinanceiro.write(dados_divida)
    novofinanceiro.close()

else:
    while conteudo:
        conteudo = financeiro.readline()
    
        if  '\n' in conteudo:
            conteudo = conteudo[:-1]
        lista_pessoas = conteudo.split('-')
        if lista_pessoas != ['']:
            lista_pessoas[0], lista_pessoas[1] = lista_pessoas[1], lista_pessoas[0]
            lista_dados.append(lista_pessoas)
        
        lista_dados.sort()

    financeiro.close()

    for dados in lista_dados:
        orgCpf = (dados[1][:3]) + '.' + (dados[1][3:6]) + '.' + (dados[1][6:9]) + '-' + (dados[1][9:12])
        falta = int(dados[3]) - int(dados[4])
        print('Nome: {:15}CPF: {:19}Cidade: {:15}\nDívida: {:10}Pago: {:10}Falta pagar: {:10}'.format((dados[0]), str(orgCpf),(dados[2]), (dados[3]), (dados[4]), str(falta)))

    verificando = input('Informe um CPF para acessar as informações: ')
    for numero in lista_dados:
        if verificando == numero[1]:
            orgCpf = (numero[1][:3]) + '.' + (numero[1][3:6]) + '.' + (numero[1][6:9]) + '-' + (numero[1][9:12])
            falta = int(numero[3]) - int(numero[4])
            print('Nome: {}\nCPF: {}\nCidade: {}\nDívida: {}\nPago: {}\nFalta Pagar: {}'.format(numero[0], orgCpf, numero[2], numero[3], numero[4], str(falta)))
    
