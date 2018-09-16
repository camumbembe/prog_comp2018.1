TempoViagem = float(input('Quanto tempo durou a viagem, em horas: '))

VelocidadeMedia = float(input('Qual foi a velocidade média durante o percurso, em km/h: '))

Distancia = TempoViagem * VelocidadeMedia

ListrosUsados = Distancia/12

print('A viagem de {0} km, que durou {1} horas, com uma velocidade média de {2} km/h, consumiu {3} litros de combustível.'.format(Distancia, TempoViagem, VelocidadeMedia, ListrosUsados))