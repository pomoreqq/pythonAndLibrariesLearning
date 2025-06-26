# Quiz – Python Basics (30 pytań)

# 🧠 Część 1: Konceptualna – zrozumienie zasad
# 1. Czym różni się `is` od `==` w Pythonie? Podaj przykład.
    #is jest to operator ktory porownuje czy dwa dane obiekty sa takie same, a == czy ich wartosci sie zgadzaja
    #a = [1,2,3]
    # b = a
     #b is a // True, b == a // true
     # b = a[:], b is a // false, b == a// True    
# 2. Jakie są podstawowe typy danych w Pythonie i do czego służą?
    #boolean,int,float,string,,tuple,list,dict,set. Sluza do reprezentowania wartosci
# 3. Wyjaśnij pojęcie "mutowalności" i wskaż przykłady typów mutowalnych i niemutowalnych.
    # mutowalnosc jest to mozliwosc do zmiany wartosci obiektu, mutowalne w pythonie kazde oprocz tuple
# 4. Co oznacza, że Python jest językiem dynamicznie typowanym?
#  Typ zmiennej nie musi być deklarowany — interpreter sam to rozpoznaje w czasie działania programu.
# 5. Kiedy stosować `elif` zamiast wielu `if`?
    #kiedy wobec jakiejs akcji mamy wiele wyborow?
# 🧩 Część 2: Operatory i wyrażenia
# 6. Napisz wyrażenie, które sprawdza czy liczba jest podzielna przez 3 i jednocześnie większa niż 100.
    # if a % 3 == 0 and a > 100
# 7. Co zwróci `not (True and False) or True`? Wytłumacz krok po kroku.
    #True? najpierw, nawias t and f daje f, not f daje t, t or t daje t
# 8. Jak działa operator `in` w kontekście stringów i list?
    #zwraca true jesli dana wartosc zostaje znaleziona w sekwencji
# 🛠 Część 3: Kod – napisz i przeanalizuj
# 9. Napisz funkcję, która przyjmuje liczbę i zwraca tekst: "parzysta" lub "nieparzysta".
    # def oddEven(a):
        #if a % 2 == 0:
            #return 'parzysta'
        #else:
            #return 'nieparzysta'
# 10. Napisz funkcję, która zwraca największą z trzech podanych liczb.
    # def returnMax(a,b,c):
        #return max(a,b,c)
# 11. Co robi poniższy kod? Wyjaśnij wynik:
#     a = [1, 2, 3]
#     b = a
#     b.append(4)
#     print(a)
        # ponizszy kod robi to: 1. jest definiowana lista A, nastepnie wartosc tej listy jest przypisywana do zmiennej b, nastepnie przy pomocy
        # funkcji list append do konca listy dodawane jest 4. nastepnie printowana jest lista a czyli [1,2,3]
# 12. Napisz funkcję is_vowel(char) zwracającą True dla samogłosek.
        #def isVowel(x):
    #         if (x == 'a' or x == 'e' or x == 'i' or 
    #           x == 'o' or x == 'u' or x == 'A' or 
    #           x == 'E' or x == 'I' or x == 'O' or 
    #           x == 'U'):
    #               return True
    #          else:
    #               return False
# 13. Napisz funkcję, która liczy ile razy dany znak występuje w stringu.
        # def charCounter(stringS):
        #   dictonaryCount = dict()
            #for i in stringS:
                #if i not in dictonaryCount:
                    #dictonaryCount[i] = 1
                #else:
                    #dictonaryCount[i] += 1
            #return dictonaryCount
# 14. Jakie są różnice między `=` a `==`? Podaj przykłady.
    #= jest to operator przypisania, == operator porowania
        #a = [1,2,3]
        #b = a // [1,2,3]
        # a == b // True
# 15. Czy `True + True + False` jest poprawne? Jeśli tak, co zwróci?
        # tak jest poprawne, zwroci int 2
# 🔁 Część 4: Pętle i warunki
# 16. Napisz pętlę, która wypisze wszystkie liczby od 1 do 20 poza wielokrotnościami 3.
    # for i in range(1,21):
        #if i % 3 != 0:
            #print(i)
# 17. Co robi range(10, 2, -2)? Wypisz elementy.
        # petla iteruje zaczyna od 10 i iteruje co -2 czyli 10,8,6,4

  
# 18. Czym różni się `while` od `for`? Kiedy używać którego?
    #for uzywamy kiedy znamu dlugosc danego iterowalnego obiektu, while gdy znamy tylko warunek petli, while nadaje sie do nieokreslonej liczby iteracji
# 19. Jak zatrzymać pętlę while jeśli użytkownik wpisze „stop”?
    # nalezy dac warunek w petli czyli 
        #inputUser = input()
        #if inputerUser == 'stop':
            #break
# 20. Napisz pętlę for, która sumuje tylko liczby parzyste z listy.
        #for i in myList:
            #sum = 0
            # if i % 2 == 0:
                #sum += i
# 🧾 Część 5: Struktury danych
# 21. Jakie są różnice między list, tuple i set?
    #list i set sa mutowalne a tuple nie
# 22. Napisz kod, który tworzy dict, w którym klucze to imiona, a wartości to ich długość.
        # for i in nameList:
            #nameDict = dict()
            # if i not in nameDict:
                #nameDict[i] = len(i)

# 23. Co robi metoda .get() w słowniku? Jakie daje korzyści?
    #zwraca wartosc pod danym kluczem
# 24. Jak dodać nowy element do set? Co się stanie jeśli dodasz ten sam dwa razy?
    # za pomoca metody .add(), dodanie nic nie zmieni dwoch tych samych bo nie przechowuje duplikatow
# 25. Co zwróci list("abc")?
        # liste, ['a','b','c']
# 🧵 Część 6: Funkcje i domknięcia
# 26. Napisz funkcję repeat(word, n) która zwraca słowo powtórzone n razy, oddzielone spacją.
# def repeat(word,n):
#     return ' '.join([word]* n)
# print(repeat('essa',3))
# 27. Jakie są korzyści z używania funkcji w programie?
        # niby takie proste pytanie a nier ewiem co odpowiedziec, modularnosc reuzywalnosc, testowalnosc
# 28. Napisz funkcję, która przyjmuje listę liczb i zwraca listę z tylko dodatnimi wartościami.
        # def listWithPositive[numberList]:
            #newList = []
            #for i in numberList:
                #if i > 0:
                    #newList.append(i)
            #return newList
# 🧪 Część 7: Błędy i formatowanie
# 29. Jakie błędy może rzucić ten kod? Jak je naprawić?
#     int("abc") + 1
        # valueError
# 30. Napisz przykład użycia try-except, który łapie błąd dzielenia przez zero.
#   try:
        #a,b=2,0
        #res = a/b
    #expect ZeroDivisionError:
        # res = 0