def tomadaDeDados(tipo):
    inputSolicitado = {
        'nota1': ['Informe a primeira nota do aluno:'],
        'nota2' : ['Informe a segunda nota do aluno:'],
        'nota3' : ['Informe a terceira nota do aluno:'],
        'nota4': ['Informe a quarta nota do aluno:'],
        'cpf' : ['Informe os números do CPF: ']
    }
    try:
        while True:
            tomada = float(input(inputSolicitado[tipo][0]))
            if tipo == 'cpf':
                if int(tomada) == 0:
                    return False
                if len(tomada) != 11:
                    print('Digite um CPF válido, 11 dígitos')
                    continue

    except:
        print('digite um numero valido')
        tomadaDeDados(tipo)


tomadaDeDados('nota1')
tomadaDeDados('nota2')
