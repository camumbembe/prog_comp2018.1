#antes do vetor:

#nome1 = input('Informe nome aluno 1: ')
#nome2 = input('Informe nome aluno 2: ')
#nome3 = input('Informe nome aluno 3: ')

#media1 = input('Informe a media de {0}: '.format(nome1))
#media2 = input('Informe a media de {0}: '.format(nome2))
#media3 = input('Informe a media de {0}: '.format(nome3))

#media_turma = (float(media1) + float(media2) + float(media3))/3

#print('A media da turma foi {0}: '.format(media_turma))

#if (float(media1) >= media_turma):
#	print('Parabens {0}'.format(nome1))

#if (float(media2) >= media_turma):
#	print('Parabens {0}'.format(nome2))

#if (float(media2) >= media_turma):
#	print('Parabens {0}'.format(nome3))

#com vetor(mesma coisa de listas):

vetor_nomes = []
vetor_medias = []
qt_alunos = 10

for contador in range(0, qt_alunos):
	nome_aluno = input('Informe o nome do aluno {0}: '.format(contador+1))
	vetor_nome.append(nome_aluno)

	media_aluno = float(input('Informe a media do aluno{0}: '.format(vetor_nome[contador])))
	vetor_medias.append(media_aluno)
print(vetor_nomes)
print(vetor_medias)

#substituir qt de alunos e o for por while
