def validarDados(dadoObtido):
    

def tomadaDeDados(dados):
    inputSolicitado = {
        'nota1': ['Informe a primeira nota do aluno: '],
        'nota2' : ['Informe a segunda nota do aluno: '],
        'nota3' : ['Informe a terceira nota do aluno: '],
        'nota4': ['Informe a quarta nota do aluno: '],
        'cpf' : ['Informe os números do CPF: ']
    }
    try:
        while True:
            tomada = float(input(inputSolicitado[dados][0]))
            if dados == 'cpf':
                if int(tomada) == 0:
                    return False
                if len(tomada) != 11:
                    print('Digite um CPF válido, 11 dígitos')
                    continue
            return tomada

    except:
        print('Digite um número válido')
        tomadaDeDados(dados)


nota1 = tomadaDeDados('nota1')
nota2 = tomadaDeDados('nota2')
print(nota1)