

slownik = dict()
licznik = dict()
with open('workingWithTextFilesSection/logi2.txt', mode='r') as f:
    content = f.readlines()
    
    for i in content:
        splittedContent = i.strip().split(':')
        if len(splittedContent) != 3:
            print('wrong line: ',i)
            continue
        nameSurname,action,date = splittedContent

        if nameSurname not in slownik:
            slownik[nameSurname] = list()
        slownik[nameSurname].append(action)


with open('workingWithTextFilesSection/raport.txt',mode='w') as f:
    for key,value in slownik.items():
        licznik = dict()
        for i in value:
            if i not in licznik:
                licznik[i] = 1
            else:
                licznik[i] += 1
        f.write(f"{key}: {licznik}\n")

        
