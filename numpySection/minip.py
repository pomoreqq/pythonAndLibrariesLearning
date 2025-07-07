import numpy as np
np.random.seed(0)
# 1. Identyfikator użytkownika (np. 100–200), 1200 wpisów
user_ids = np.random.randint(100, 201, size=1200)

# 2. Dopasowanie modelu (float: 0.0–1.0)
match_scores = np.random.rand(1200)

# 3. Czy użytkownik kliknął „Sprawdź produkt” (1 = tak, 0 = nie)
clicked = np.random.choice([0, 1], size=1200, p=[0.6, 0.4])

# #1. Ogólny performance modelu
# Średni match_score w całym zbiorze okolo 0,511
meanMatchScore = np.mean(match_scores)

# Jaki był CTR (click-through-rate)? 39,8%
ctr = (clicked[clicked == 1].sum() / 1200) * 100 

# Ile było unikalnych użytkowników? / 101 unikalnych  uzytkownikow
uniqueUsers = np.unique(user_ids)


# 2. Zachowania użytkowników
# Ilu użytkowników kliknęło przynajmniej raz?  101 unikalnych userow przynajmniej raz kliknelo
indexesOfClick = np.where(clicked == 1)[0]
usersWithOneClick = user_ids[indexesOfClick]
numberOfUsersWithAtleastOneClick = len(np.unique(usersWithOneClick))

# Ilu użytkowników miało 10 lub więcej rekomendacji? // 67
user,count = np.unique(user_ids,return_counts=True)
userWithMoreThanTen = user[count > 10]
lenOfUsersWithMoreThanTen = len(userWithMoreThanTen)
# print(lenOfUsersWithMoreThanTen)
# Jaki był średni match_score dla użytkowników, którzy nie kliknęli ani razu?

