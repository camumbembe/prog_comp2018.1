letras = 'ABCDE'
gabarito  = ''
g = r = contador = acerto = erro =0
resposta_aluno = ''


while g < 5:
    professor = input('Informe o gabarito da prova: ').upper()
    if professor not in letras:
        print('Letra inválida, digite novamente.')
        continue
    else:
        g+= 1
        gabarito = gabarito + professor
print('Gabarito = {0}'.format(gabarito))


while r < 5:
    aluno = input('Informe as respostas do aluno: ').upper()
    if aluno not in letras:
        print('Letra inválida, digite novamente.')
        continue
    else:
        r+= 1
        resposta_aluno = resposta_aluno + aluno
print('Resposta aluno = {0}'.format(resposta_aluno))

for element in gabarito:
    if element == resposta_aluno[contador]:
        print('Resposta correta')
        acerto += 1
    else:
        print('Resposta incorreta')
        erro += 1
    contador +=1

print('O gabarito da prova é: {0}, a resposta do aluno foi: {1} e a quantidade de acertos foi: {2}'.format(gabarito, resposta_aluno, acerto))
