

dicttonary = dict()
with open('workingWithTextFilesSection/logi.txt',mode='r') as f:
    content = f.readlines()
    
    for i in content:
        splittedContent = i.strip().split(':')
        if len(splittedContent) != 2:
            print('invalid line')
            continue
        if splittedContent[0] not in dicttonary:
            dicttonary[splittedContent[0]] = set()
         
        dicttonary[splittedContent[0]].add(splittedContent[1])


with open('workingWithTextFilesSection/aktywni.txt', mode='w') as f:
    for key,actions in dicttonary.items():
        if len(actions) > 1:
            f.write(f"{key}:{','.join(actions)}\n")

