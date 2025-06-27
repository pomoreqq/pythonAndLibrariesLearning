# Quiz: String Manipulation and Text Methods in Python (25 questions)

# 1.
# Co zwróci wynik: "Hello World".lower() ?
    #hello world
# 2.
# Jakiej metody użyjesz, aby sprawdzić, czy tekst zaczyna się od konkretnego znaku lub słowa?
    #startswith()
# 3.
# Jakiej metody użyjesz, aby zamienić wszystkie spacje w tekście na myślniki?
    #replace()
# 4.
# Co robi metoda .strip()?
    #usuwa biale znaki ze stringu
# 5.
# Jak sprawdzić, czy cały tekst zawiera tylko cyfry?
    #iterowac po stringu i sprawdzac wszszystko metoda isdigit()
# 6.
# Jak połączyć listę stringów ["a", "b", "c"] w jeden string z separatorem "-"?
    # -.join(list)
# 7.
# Co zwróci: "Python".find("t") ?
    # 2
# 8.
# Czym się różni .find() od .index()?
    #fin jesli nie znajdzie wartosci zwroci -1 a index zwroci expection
# 9.
# Co zwróci wyrażenie: "data".replace("a", "x", 1)
# dxta
# 10.
# Jakiej metody użyjesz, by policzyć liczbę wystąpień znaku 'a' w stringu?
    # count()
# 11.
# Jak sprawdzić, czy string zawiera tylko małe litery?
    #metoda islower()
# 12.
# Co robi .title() ?
    #powoduje uppercase kazdego slowa 1 litery
# 13.
# Co oznacza slicing [::-1] dla stringa?
    #zwroci go od tylu
# 14.
# Co robi metoda .split(",") ?
    #dzieli stringa wobec przecinka
# 15.
# Której metody użyć, by sprawdzić, czy tekst kończy się określonym znakiem?
    #endswith()
# 16.
# Jak zamienić pierwszą literę każdego słowa na wielką?
    # metoda .title()
# 17.
# Czym różni się .isalpha() od .isalnum() ?
    # isalpha zwraca true jesli wszystke chars w stringu sa z alfabetu, a isalnum ze wszystkie litery sa w stringu z alfabetu i lub numerami
# 18.
# Kiedy metoda .format() jest przydatna?
    #gdy chcemy wyprimnotwac stringa z zmiennymi
# 19.
# Jak sformatować string z dokładnością do 2 miejsc po przecinku dla liczby zmiennoprzecinkowej?
    # .2f
# 20.
# Co zwraca "{} + {} = {}".format(2, 3, 5) ?
    #"2 + 3 = 5"
# 21.
# Jakiego znaku używamy do wstawiania nowej linii w stringach?
    # \n
# 22.
# Jak wypisać drugi znak stringa "Python"?
    # string = 'Python'
    # print(string[1])
# 23.
# Co robi metoda .center(10, "-") ?
    # powoduje powstanie  myslnikow przed i po stringu
# 24.
# Czy metoda .startswith() rozróżnia wielkość liter?
    #taj
# 25.
# Co się stanie jeśli .format() otrzyma mniej argumentów niż {} w stringu?
    # Jeśli .format() otrzyma mniej argumentów niż {} – błąd runtime (IndexError). Czyli tak: error – poprawnie, ale warto doprecyzować nazwę błędu.
