lista_nomes = []
lista_medias = []
qt_alunos = 0

while qt_alunos < 5:
    nome_aluno = input('Informe o nome do aluno: ')
    lista_nomes.append(nome_aluno)

    media_aluno = float(input('Informe a média do aluno {0}: '.format(nome_aluno)))
    lista_medias.append(media_aluno)
    qt_alunos +=1

print(lista_nomes)
print(lista_medias)

