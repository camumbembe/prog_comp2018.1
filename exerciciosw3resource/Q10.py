
for elements in range(1, 51):
    if elements % 3 == 0:
        if elements  % 5 == 0:
            print('fizzbuzz')
        else:
            print('fizz')
    elif elements % 5 == 0:
        print('buzz')
    else:
        print(elements)

    
