
listOfDictonaries = list()

with open('workingWithTextFilesSection/klienci.txt') as f:
    content = f.readlines()
    for i in content:
        splittedLine = i.strip().split(',')
        if len(splittedLine) != 3:
            print('wrong line:', i)
            continue
        try:
            name,surname,age = splittedLine 
            age =  int(age)
            if bool(name) and bool(surname):    
                listOfDictonaries.append({
                    'name':name,
                    'surname':surname,
                    'age': age})
            else:
                print('name or surname is empty')
        
        except ValueError:
                print('is not integer', age)
        
        


with open('workingWithTextFilesSection/poprawni.txt',mode ='w') as f:
     for i in listOfDictonaries:
          name,surname,age  = i.values()
          f.write(f"{surname} {name} - {age} lat\n")