
from datetime import datetime

dane = open('pythonSection/minizadania/datylogi.txt', mode ='r')

def convert(dateString):
    format = '%Y-%M-%d'
    toDate = datetime.strptime(dateString,format).date()
    return toDate


d = dict()
for i in dane:
    data = i.strip().split(':')
    if len(data) != 2:
        print(f'error wrong line: {i}')
        continue
    user,date = data
    day = convert(date).strftime('%A')
    if user not in d:
        d[user] = dict()
    if d[user].get(day):
        d[user][day] += 1
    else:
        d[user][day] = 1

print(d)    
dane.close()