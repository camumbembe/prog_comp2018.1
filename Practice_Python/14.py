list2 = [1,23,4,5,7,9,11,14,5,6,7,9,10,17]

while True:
    content = int(input('Enter a number to form a list: '))
    list2.append(content)
    if content == 0:
        break

list2 = set(list2)

print(list2)