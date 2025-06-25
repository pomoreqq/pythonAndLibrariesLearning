

# Task: Track unique actions per user from a log file
# The file `file.txt` contains lines in the format: user:action
# Each line represents a user performing an action.
# Malformed lines (not exactly two parts) should be skipped with a warning.
# Build a dictionary where each key is a user and the value is a set of unique actions performed by that user.
# Print the resulting dictionary.
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
    



