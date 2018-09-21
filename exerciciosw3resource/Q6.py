numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

even = 0

odd = 0

for element in numbers:
	if element % 2 == 0:
		even = even + 1
	else:
		odd = odd + 1
print('In the informed list {0} numbers are even and {1} numbers are odd'.format(even,odd))
