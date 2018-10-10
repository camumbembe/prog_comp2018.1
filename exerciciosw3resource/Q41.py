ano = int(input('Informe um ano: '))
mes = int(input('Informe um mes [1-12]: '))
dia = int(input('Informe um dia[1-31]: '))

trinta = 4,6,9,11
trinta_um = 1, 3,5,7,8,10,12


if dia == 31 and mes == 12:
    dia = 1
    mes = 1
    ano += 1
elif dia == 30 and mes in trinta:
    dia = 1
    mes +=1
elif dia == 31 and mes in trinta_um:
    dia = 1
    mes +=1
else: 
    dia +=1

print('A próxima data é {0}/{1}/{2}'.format(dia, mes, ano))
