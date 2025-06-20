




txt = open('pythonSection/minizadania/log.txt', mode='r')

 

d = dict()

for i in txt:
    firstCzesc = i.split(':')[0]
    if  firstCzesc not in d:
        d[firstCzesc] = 1
    else: 
        d[firstCzesc] += 1
    

        


print(d)
