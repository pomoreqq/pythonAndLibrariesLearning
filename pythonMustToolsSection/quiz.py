# 🔧 Quiz: Must-Know Python Tools – 20 Pytań (czysta wersja)

# 1. Co zwraca funkcja range(5)?
        # 0,1,2,3,4
# 2. Jak działa range(2, 10, 2)?
        # 2,4,6,8
# 3. Ile razy wykona się pętla zagnieżdżona: for i in range(3): for j in range(2): pass?
        #  i[0],j[0]j[1], i[1]j[0]j[1], i[2]j[0]j[1], nie rozumiem pytania petla zagniedzona wykona sie 6 razy
# 4. Jak stworzyć listę wszystkich liczb parzystych od 0 do 10 przy użyciu list comprehension?
# listof = [x for x in range(11) if x%2 == 0]

# 5. Co robi funkcja map() i jakie przyjmuje argumenty?
    #powoduje nalozenie  funkcji na iterowalny obiekt i zwraca map obiekt, przyjmuje arguemnty funkcja,iterowalny obiekt
# 6. Czym różni się filter() od map()?
    # zwraca iterowalny obiekt a nie map obiekt
# 7. Do czego służy funkcja lambda w Pythonie?
    #do pisania krotkich anonimowych funkcji, przydaje sie np do pandas w metodzie apply do przeksztalcen dataframe
# 8. Napisz wyrażenie lambda, które podnosi liczbę do kwadratu.
    # lambda x: x**2
# 9. Jak przekształcić listę stringów ['1', '2', '3'] na listę liczb całkowitych?
    # map(int,listofstrings)
# 10. Jak za pomocą list comprehension odfiltrować tylko elementy większe niż 5 z listy?
    # list = [x for x in examplelist if  x > 5]
# 11. Do czego służy funkcja any()?
    # sprawdza czy chociaz jedna z iterowalnego obiektu jest true
# 12. Do czego służy funkcja all()?
    #sprawdza czy wszystkie wartosci w iterowalnym obiekcie sa true
# 13. Jak uzyskać długość każdego słowa w liście ['python', 'is', 'fun']?
        #iterowac w petli bo liscie i sprawdzac len kazdej wartosci obiektu
# 14. Napisz wyrażenie, które zamienia wszystkie litery w liście ['a', 'b', 'c'] na wielkie.
        # map(lambda x: x.upper(),list)
# 15. W jaki sposób posortować listę stringów według długości (rosnąco)?
        #sortedlist = sorted(list,key=len)
# 16. Co robi konstrukcja: [x for x in lista if x % 2 == 0]?
    # zwraca takie x w liscie ktore spelnia warunek
# 17. Jak zagnieździć 3 pętle for wewnątrz siebie w Pythonie?
    #for i in range(10):
        #for j in range(10):
            #for k in range(10):
# 18. Jakie są zalety używania list comprehension w porównaniu do klasycznych pętli?
    # sa o wiele bardziej czytelne
# 19. Czym różni się wywołanie list(map(...)) od samego map(...)?
    # ze zwraca liste
# 20. Jak wyodrębnić elementy zagnieżdżonej listy [[1, 2], [3, 4]] do jednej płaskiej listy?
    # [element for innerList in list for element in innerList]