a = [1, 2, 3]
b = [4, 5, 6]

def dotproduct(a,b):
    listforsum = list()
    dotsum = 0
    for i in range(len(a)):
        listforsum.append(a[i] * b[i])
    dotsum = sum(listforsum)
    return dotsum


print(dotproduct(a,b))


def dotproduct(a, b):
    return sum(a[i] * b[i] for i in range(len(a)))

def dotproduct(a, b):
    return sum(x * y for x, y in zip(a, b))