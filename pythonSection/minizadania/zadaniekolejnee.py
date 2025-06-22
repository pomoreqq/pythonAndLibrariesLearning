



dane = open('pythonSection/minizadania/oceny.txt', mode='r')

d = dict()
for i in dane:
    splittedDane = i.strip().split(':')
   
    if len(splittedDane) != 3:
        print(f'nielwasciwa linia zostaje pominieta: {i}')
        continue
    if splittedDane[0] not in d:
        d[splittedDane[0]] = list()
    d[splittedDane[0]].append(splittedDane[2])


for key,value in d.items():
    suma = sum(map(float,value))
    srednia = suma / len(value)
    print(f'{key} - srednia - {srednia}')
        

   
    
    