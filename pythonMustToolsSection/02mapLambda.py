numbers = [1, 2, 3, 4, 5, 6]

newList = map(lambda x: 'even' if  x % 2 == 0 else 'odd',numbers)
print(list(newList))