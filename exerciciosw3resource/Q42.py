# listanumeros = []
# user_input = ''

# while user_input != 0 :
#     user_input = int(input('Informe valores para calcular a soma e média e entre com 0 para encerrar: '))
#     if user_input != 0:
#         listanumeros.append(user_input)

# media = sum(listanumeros)/len(listanumeros)
# print('Os números informados foram {0}, a soma deles é = {1} e a média é de {2}'.format(listanumeros, sum(listanumeros), media))

#fazendo com o que foi ensinado

user_input = ''
somanumeros =int( )
numeros = int( )

while user_input != 0 :
    user_input = int(input('Informe valores para calcular a soma e média e entre com 0 para encerrar: '))
    if user_input != 0:
        somanumeros = user_input + somanumeros
        numeros += 1

media = somanumeros / numeros

print('A soma dos números é = {0} e a média é = {1}'.format(somanumeros, media))
