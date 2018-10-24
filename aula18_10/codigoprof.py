import random

# --------------------------------------------------------------------------
# Função para gerar uma lista com 5 números inteiros aleatórios 
# dentro de um intervalo especificado
def gera_lista(intValorInicial, intValorFinal):
   lista    = []
   contador = 0
   while contador < 5:
      numero = random.randint(intValorInicial, intValorFinal)
      if numero not in lista:
         lista.append(numero)
         contador += 1
   return lista
# --------------------------------------------------------------------------


cartela_bingo = []

# Gerando e adicionando os numeros da letra B na lista cartela_bingo
cartela_bingo.append(gera_lista(1, 15))

# Gerando e adicionando os numeros da letra I na lista cartela_bingo
cartela_bingo.append(gera_lista(16, 30))

# Gerando e adicionando os numeros da letra N na lista cartela_bingo
cartela_bingo.append(gera_lista(31, 45))

# Gerando e adicionando os numeros da letra G na lista cartela_bingo
cartela_bingo.append(gera_lista(46, 60))

# Gerando e adicionando os numeros da letra O na lista cartela_bingo
cartela_bingo.append(gera_lista(61, 75))

print(cartela_bingo)