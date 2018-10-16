numero = '1234567890'
letra = 'QWERTYUIOPASDFGHJKLZXCVBNM'
caracter = '@#&'
checkNumero = checkLetra = checkCaracter = 0

# while True:
#     senha = input('Informe sua senha de cinco caracteres: ')
#     if len(senha) != 5: 
#         senha = input('Informe sua senha de exatamente cinco caracteres: ')
#     if len(senha) == 5:
#         break

senha = input('Informe sua senha de cinco caracteres: ')
while True:
    for element in senha:
        if element in numero:
            checkNumero +=1
        if element in letra:
            checkLetra +=1
        if element in caracter:
            checkCaracter +=1

    if len(senha) == 5 and checkNumero > 0 and checkLetra > 0 and checkCaracter > 0: 
        print('Senha dentro dos padrões.')
        break
    else:   
        if len(senha) != 5:
            print('O tamanho da sua senha deve conter exatamente cinco caracteres.')
        if checkNumero == 0:
            print('Sua senha deve conter, pelo menos, um número.')
        if checkLetra == 0:
            print('Sua senha deve conter, pelo menos, uma letra maiúscula.')
        if checkCaracter == 0:
            print('Sua senha deve conter, pelo menos, um dos caratéres especiais.')
        senha = input('Informe sua senha dentro do padrão: ')  
  
senha2 = input('Informe a senha novamente para verificação: ')
while True:
    if senha == senha2:
        print('Senha OK')
        break
    else:
        print('Senha incorreta.')
        senha2 = input('Informe a senha novamente: ')




