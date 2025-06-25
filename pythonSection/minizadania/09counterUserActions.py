
# Task: Count user activity from a list of logs
# You are given a list of dictionaries where each entry has a user and an action.
# Count how many times each user appears in the log (i.e. total number of actions).
# Return the result as a dictionary: {user: action_count}

logi = [
    {"user": "Anna", "action": "login"},
    {"user": "Tomek", "action": "upload"},
    {"user": "Anna", "action": "logout"},
    {"user": "Kasia", "action": "login"},
    {"user": "Tomek", "action": "download"},
    {"user": "Anna", "action": "upload"},
    {"user": "Piotr", "action": "login"},
    {"user": "Kasia", "action": "logout"},
]


unikalne = set()

for i in logi:
    wpis = i['user']
    unikalne.add(wpis)


d = dict()

for i in logi:
    user = i['user']
    if user not in d:
        d[user] = 1
    else:
        d[user] += 1



print(d)