result = ''

divisivel = ''

for number in range (199, 204):
    for element in str(number):
        if int(element) % 2 == 0:
            divisivel = divisivel + element
        else:
            divisivel = ''
            break
    result = result + divisivel + ','
    divisivel = ''
print(result)