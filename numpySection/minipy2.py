import numpy as np
np.random.seed(0)

# 1000 rekordów sesji
user_ids = np.random.randint(100, 200, size=1000)  # user_id od 100 do 199
session_lengths = np.random.normal(loc=300, scale=50, size=1000).round()  # czas sesji w sekundach
course_ids = np.random.randint(1, 11, size=1000)  # kursy 1–10
clicks = np.random.randint(0, 6, size=1000)  # liczba kliknięć 0–5


#1️⃣ Średnie zachowanie użytkownika
# Oblicz średnią długość sesji na całym zbiorze / 301,225 sekund
meanSession = np.mean(session_lengths)

# Oblicz średnią liczbę kliknięć 2.4
meanClicks = np.mean(clicks)

# Ilu użytkowników (unikalnych) korzystało z platformy? // 100

lenOfUniqueUsers = len(np.unique(user_ids))

# 2️⃣ Analiza aktywnych i pasywnych użytkowników
# Ilu użytkowników miało przynajmniej jedną sesję z 0 kliknięć? // 194
user_ids_with_zero_clicks = user_ids[clicks == 0]
unique_users_with_zero_clicks = np.unique(user_ids_with_zero_clicks)
number_of_users = len(unique_users_with_zero_clicks)

# Ilu użytkowników średnio klika 4 lub więcej razy (na swoje sesje)? 328
unique_users = np.unique(user_ids)
high_click_users = []

for user in unique_users:
    user_clicks = clicks[user_ids == user]
    if np.mean(user_clicks) >= 4:
        high_click_users.append(user)

len_of_users = len(high_click_users)
# Jaka jest średnia długość sesji dla użytkowników, którzy nie klikają w ogóle? 304 sekundy
# meanOfSessionWithZeroClicks = np.mean(session_lengths[indiciesWithZeroClick])
# 3️⃣ Analiza kursów
# Który kurs miał najdłuższy łączny czas spędzony (suma sesji)? kurs nr 6
totalTimes = []
uniqueCourses = np.unique(course_ids)

for course in uniqueCourses:
    mask = course_ids == course
    totalTime = np.sum(session_lengths[mask])
    totalTimes.append(totalTime)

indxMax = np.argmax(totalTimes)
courseWithMaxSessions = uniqueCourses[indxMax]

# Który kurs miał najwięcej kliknięć łącznie? kurs nr 6
totalClicks = []
for course in uniqueCourses:
    mask = course_ids == course
    totalClick = np.sum(clicks[mask])
    totalClicks.append(totalClick)
idxMaxClicks = np.argmax(totalClicks)
courseWithMostClicks = uniqueCourses[idxMaxClicks]
# print(courseWithMostClicks)
# Ile kursów miało średni czas sesji poniżej 280 sekund? nie bylo takiego kursu

coursesWithMeanBelow280secs = []
for course in uniqueCourses:
    mask = course_ids == course
    meanOfCourse = np.mean(session_lengths[mask])
    if meanOfCourse < 280:
        coursesWithMeanBelow280secs.append(meanOfCourse)

print(coursesWithMeanBelow280secs)