# 📘 QUIZ – WORKING WITH TEXT FILES (Sekcja + Rozszerzenia tematyczne)

# 1. Co zwraca metoda `.readlines()`? Podaj przykład wyniku.
        #zwraca liste stringow zakonczonych nowa linia az do pustego stringa
        #example.txt / siema
        #              siema
        #f = open('example.txt', mode='r')
        #print(f.readlines())
        # // ['siema\n','siema\n']
# 2. Dlaczego `with open(...)` jest bezpieczniejsze od `open()` bez `with`?
        #bo odrazu zamyka plik
# 3. Jaka jest różnica między trybem `'r'`, `'w'`, `'a'` i `'x'` w `open()`?
    # miedzy r = sluzy do odczytu pliku
    # w sluzy do pisania w pliku,
    # a sluzy do dopisywania na koniec pliku
    # x sluzy do pisania do pliku ale jak plik istnieje o tej nazwie to wywali error
# 4. Wyjaśnij, jak działa poniższy kod:
#    with open("plik.txt") as f:
#        lines = f.readlines()
#        print(lines[0])
#      #wczytuje plik.txt jako f, zapisuje w zmiennej lines linie pliku, printuje tylko pierwsza linie
# 5. Co się stanie, jeśli nie zamkniesz pliku otwartego bez `with`?
    #bedzie caly czas otwarty
# 6. Jak poradzić sobie z wczytaniem pliku, w którym część linii ma złą strukturę?
    # trzeba przy wczytywaniu linii np do zmiennej dac if statment ktory spowoduje odrzucenie zlej lini w petli
# 7. Co oznacza `split(':')` w kontekście linii tekstowej? Podaj przykład użycia.
    # powoduje podzial linii wobec znaku dwukropka
    # np linia = 'a:b:c'
        #splittedLinia = linia.split(':')

# 8. W jaki sposób można użyć `set()` do usunięcia duplikatów z listy logów?
    #nalezy w petli dodawac do danego klucza logi
# 9. Z czego wynikają błędy konwersji typu (np. `ValueError: invalid literal for int()`) podczas czytania pliku?
    #z powodu wystepowania np bialych znakow
# 10. Jak zbudować słownik `user -> lista akcji` na podstawie danych tekstowych?
        #otworzyc plik do przeczytania, i zapisac w zmiennej otwarty plik, nastepnie iterowac po zmiennej i dodawac do np slownika jako key user a akcje jako valu tego keya

# 11. Czym różni się zapis `f.write("Hello\n")` od `f.writelines()`?
# 12. Co się stanie, jeśli otworzysz plik w trybie `'w'` i zapiszesz do niego 2 razy?
# 13. Dlaczego warto używać `.strip()` przed `split()`?
# 14. Jak przekształcić dane `Anna,Nowak,29` do formatu `Nowak Anna - 29 lat`?
# line = "Anna,Nowak,29"
# name, surname, age = line.split(',')
# formatted = f"{surname} {name} - {age} lat"
# 15. Jak sprawdzić, czy linia składa się dokładnie z 3 pól?
    #write zapisuje stringi do pliku, a writelines z listy stringow zapisuje
# 16. Czym się różni `.read()` od `.readlines()` przy dużym pliku?
    #read zapisuje wszystko jako jeden string a readlines jako liste stringow
# 17. Kiedy warto używać `try/except` przy parsowaniu pliku?
    #kiedy chcemy przekonwertowac ze stringa liczbe na int
# 18. Jak zapisać dane tylko tych użytkowników, którzy wykonali więcej niż jedną unikalną akcję?
    # log_dict = {}

# with open("log.txt") as f:
#     for line in f:
#         user, action = line.strip().split(':')
#         log_dict.setdefault(user, set()).add(action)

# # Filtracja
# for user, actions in log_dict.items():
#     if len(actions) > 1:
#         print(user, actions)
# 19. Co oznacza format: `name:action:date` i jak można go walidować?
    #moze go walidowac poprzez sprawdzenie czy po splicie : dlugosc listy wynosi 3, no zwykly format informacji to jest
# 20. Jak przetwarzać duże pliki linia po linii bez wczytywania całości do pamięci?
    #with open("bigfile.txt", 'r') as f:
    # for line in f:
    #     process(line)  # np. print(line)
# 21. Jakie są dobre praktyki przy zapisie plików tekstowych zawierających dane wielopolowe (np. CSV)?
    #sprawdzenie delimitera, struktury pliku csv
# 22. Czym się różni plik `.txt` od `.csv`, jeśli oba są rozdzielane przecinkami?
    #.csv to plik sformatowany tabelarycznie (z nagłówkami i separatorami np. , lub ;) i używany do danych strukturalnych.
#.txt to ogólny plik tekstowy – może być dowolny format, bez struktury. Nawet jeśli używa przecinków, to nie znaczy, że jest tabelaryczny.

# 23. Co się stanie, jeśli zapiszesz dane z `dict` do pliku bez konwersji na tekst? 
    #data = {"name": "Anna", "age": 30}
# with open("out.txt", "w") as f:
#     f.write(data)  # BŁĄD: TypeError

# # Poprawnie:
# import json
# with open("out.txt", "w") as f:
#     json.dump(data, f)
# # 24. Jak działa metoda `.join()` w zapisie listy do pliku jako jednej linii?
# 25. Co robi `','.join(lista)` i w jakim celu używa się tego przy zapisie?
        # uzywa sie zeby rozdzielic linie przecinkami
# 26. Jaka jest różnica między `pandas.read_csv()` a `open()+split()`?
    #no pandas odrazu zapisuje zawartoscsv w dataframe czyli arrayu2d, a open i split uzywaa sie do zapisu w slowniku
# 27. Co robi parametr `index_col` w `pd.read_csv()` i kiedy warto go używać?
    #parametr ten ustawia dana kolumne na index, np w wczytywaniu plikow csv gdy chcemy inny index niz numeryczny
# 28. W jakim celu stosuje się `squeeze=True` podczas wczytywania plików w pandas?
    #ten parametr jest depracated nie uzywa sie go
# 29. Jakie problemy mogą wystąpić przy użyciu `np.loadtxt()` do plików zawierających tekst?
    #jesli wystepuje blad to plik nie zaladuje sie, dlatego uzywa sie np.genfromtext
# 30. Jakie rozszerzenie pliku sugeruje użycie `json.load()` zamiast `readlines()`?
    #rozszerzenie .json

# 💬 Wskazówka: Odpowiedzi pisz kodowo lub opisowo – zależnie od pytania.
