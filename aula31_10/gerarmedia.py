
import statistics 

arquivo = open('notas_alunos.txt', 'r')

lista_notas = []

conteudo  = arquivo.readline()
linha = conteudo[:-1].split(';')
lista_notas.append(linha)

while conteudo:
	conteudo = arquivo.readline()
	linha = conteudo[:-1].split(';')
	lista_notas.append(linha)


arquivo.close()

lista_notas.pop()

for auxiliar in range(0, len(lista_notas)):
matricula = 
nota1 = float(
nota2 = 
nota3=
nota4 =
media = (nota1+nota2+nota3 +nota4)/4

	
