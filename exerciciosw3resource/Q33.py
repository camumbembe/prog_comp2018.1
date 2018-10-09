mes = input('Informe um mes e veja quantos dias tem: ')

trinta = 'abril, junho, setembro, novembro'
trinta_um = 'janeiro, março, maio, julho. agosto, outubro, dezembro'


if mes in trinta:
    print('{0} tem 30 dias'.format(mes))
elif mes in trinta_um:
    print('{0} tem 31 dias'.format(mes))
else:
    print('Fevereiro pode ter 28 ou 29 dias')