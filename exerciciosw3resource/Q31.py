dog_human = int(input('Informe a idade do seu dog para descobrir quantos anos caninos ele tem: '))

dog_age = 0


if dog_human < 3:
    dog_age = dog_human * 10.5
else:
    dog_age = (dog_human -2) * 4 + 21


print('You dog have {0} years in human years'.format(dog_age))