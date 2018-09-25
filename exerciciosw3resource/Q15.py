senha = input('Informe sua senha a para validacao: ')

letter = 'qwertyuiopasdfghjklzxcvbnm'
number = '1234567890'
character = '!@#$%¨&*'
#min.len(senha) = 6
#max.len(senha) = 16

for element in senha:
    if letter in senha:
        print('Letter: ok')
    else:
        print('Try again with the correct letters')
    if number in senha:
        print('Number: ok')
    else:
        print('Try again with the correct numbers')
    if character in senha:
        print('Character: ok')
    else:
        print('Tray again with the correct characters')
   # if min.len(senha) == 6:
  #      print('Minimun lenght is ok')
   # else:
    #    print('The password is too small ')
    #if max.len(senha) == 13:
     #   print('The password is the correct size')



