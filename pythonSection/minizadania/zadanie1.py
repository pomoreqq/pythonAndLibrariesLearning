


dane = open('pythonSection/minizadania/file.txt', mode='r')

dictonary = dict()
for i in dane:
    splittedDane = i.strip().split(':')
    
    if len(splittedDane) != 2:
        print(f'niewlasciwa linia {i}')
        continue
    user,action = splittedDane
    if user not in dictonary:
        dictonary[user] = set()
    
    dictonary[user].add(action)
    
   
        
dane.close()

print(dictonary)
    



