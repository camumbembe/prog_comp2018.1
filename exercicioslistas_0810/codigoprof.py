# Importando a biblioteca para execução de comandos SHELL
import os

# Lipando a Tela
os.system('clear')

# Declarando as variáveis
vetNomes = []
vetNotas = []
qtAlunos = 5
somaNotas = 0

for contador in range(0, qtAlunos):
   # Lendo o nome do aluno
   nome = input('Informe o nome do aluno: ')
   # Inserindo o nome do aluno na lista de nomes
   vetNomes.append(nome)

   # Lendo a nota do aluno
   nota = float(input('Informe a nota do aluno {0}: '.format(vetNomes[contador])))
   vetNotas.append(nota)

   print('')

   somaNotas = somaNotas + vetNotas[contador]


# Lipando a Tela
os.system("clear")

# Exibindo a média da turma
mediaTurma = somaNotas/qtAlunos
print('=====================================================================')
print('A média da turma foi {0:.1f}'.format(mediaTurma))
print('=====================================================================')

# Exibindo a lista de Alunos com média acima da média da turma 
print('Nome do Aluno                                           Nota do Aluno')
for contador in range(0, qtAlunos):
	if (vetNotas[contador] >= mediaTurma):
		print('{0:30} {1:.1f} Ok!'.format(vetNomes[contador].upper(), vetNotas[contador]))
		print('---------------------------------------------------------------------')
	else:
		print('{0:30} {1:.1f} Erro!'.format(vetNomes[contador].upper(), vetNotas[contador]))
		print('---------------------------------------------------------------------')
print('=====================================================================')


