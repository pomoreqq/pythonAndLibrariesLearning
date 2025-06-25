

# Task: Count log entry occurrences by key
# You are given a text file `log.txt` where each line starts with a key, followed by a colon (e.g. "ERROR: Something went wrong").
# Count how many times each unique key appears (e.g. ERROR, INFO, WARNING).
# Print the result as a dictionary: {key: count}



txt = open('pythonSection/minizadania/log.txt', mode='r')

 

d = dict()

for i in txt:
    firstCzesc = i.split(':')[0]
    if  firstCzesc not in d:
        d[firstCzesc] = 1
    else: 
        d[firstCzesc] += 1
    

        


print(d)
