# Task 01: Calculate average grades from file
# The file `oceny.txt` contains student data in the format: name:subject:grade
# Some lines may be malformed (e.g. missing parts) — these should be skipped with a warning.
# For each student, calculate and print their average grade.


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
        

   
    
    