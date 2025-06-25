# Zadanie 2: Filtrowanie danych z JSON
# Wybierz z listy tylko tych użytkowników, którzy są aktywni i mają score >= 80.


data = [
  {"name": "Alice", "active": True, "score": 85},
  {"name": "Bob", "active": False, "score": 91},
  {"name": "Charlie", "active": True, "score": 78}
]


# listOfDicts = list()

# for i in data:
#     active,score = i['active'],i['score']
#     if active == True and score >= 80:
#         listOfDicts.append(i)
    
# print(listOfDicts)

# drugie rozwiazanie 
listOfFiltered = list()
filteredUsers = [user for user in data if user['active'] == True and user['score'] >= 80]
print(filteredUsers)