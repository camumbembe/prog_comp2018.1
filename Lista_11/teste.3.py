def validarDados(dadoObtido, tipoDeDado):
    print(str(dadoObtido))
    if tipoDeDado == 'cpf':
        if int(dadoObtido) == 0:
            return False
        if len(str(dadoObtido)) != 11:
            print('Digite um CPF válido, 11 dígitos')
            tomadaDeDados(tipoDeDado)
        else:
            return dadoObtido


def tomadaDeDados(dados):
    inputSolicitado = {
        'nota1': ['Informe a primeira nota do aluno: '],
        'nota2' : ['Informe a segunda nota do aluno: '],
        'nota3' : ['Informe a terceira nota do aluno: '],
        'nota4': ['Informe a quarta nota do aluno: '],
        'cpf' : ['Informe os números do CPF: ']
    }
    try:
        if 'nota' in dados: 
            tomada = float(input(inputSolicitado[dados][0]))
            print(tomada, 'nota')
        elif 'cpf' in dados:
            tomada = int(inputSolicitado[dados][0])
    except KeyError:
        print('Digite um número válido')
        tomadaDeDados(dados)
    else:
        return validarDados(tomada, dados)


cpf1 = tomadaDeDados('cpf')
print(cpf1)