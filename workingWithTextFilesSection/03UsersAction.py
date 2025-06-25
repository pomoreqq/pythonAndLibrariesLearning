
# Zadanie: Raport z aktywności użytkowników
# Wczytaj dane z pliku 'logi2.txt' w formacie: imię_nazwisko:akcja:data.
# Pomiń linie o niepoprawnym formacie (nie zawierające dokładnie dwóch dwukropków).
# Dla każdego użytkownika zlicz, ile razy wykonał każdą akcję.
# Wynik zapisz do pliku 'raport.txt' w formacie:
# imię_nazwisko: {'akcja1': liczba, 'akcja2': liczba, ...}
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

        
