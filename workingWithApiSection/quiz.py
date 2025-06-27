# 📋 Quiz: APIs in Python – GET, JSON, Parameters, Pagination (25 pytań)

# 1. Co to jest API i jaką rolę pełni w aplikacjach?
    # aplication programming interface, pelni forme pomostu miedzy dwoma systemami informatycznymi
# 2. Jakie są podstawowe różnice między zapytaniami GET a POST?
        #get ssluzy do wysylania zapytania i pobierania informacji
        #post ma payload i sluzy do wysylania informacji
# 3. W jakim formacie dane najczęściej są zwracane przez API?
    #json
# 4. Do czego służy biblioteka `requests` w Pythonie?
    #to wykonywania zapytan do api
# 5. Jak wykonać zapytanie GET w Pythonie z użyciem requests?
        #import requests
        # x = request.get('example')
# 6. Co zwraca metoda `.json()` na odpowiedzi z API?
        #sluzy do parsowania response z json na dictonary
# 7. Co oznacza status code 200 w odpowiedzi z API?
    # ze request powiodl sie
# 8. Jak obsłużyć sytuację, gdy API zwraca kod 404?
    # za pomoca try-expect
# 9. Czym jest parametr w zapytaniu GET?
    # sa to np informacie do query do danego api
# 10. Jak dodać parametry do zapytania GET w `requests.get(...)`?
        # params = 'example parm'
        #request.get(params=params)
        #request.get({'param': param
        #})
# 11. Co oznacza termin "pagination" w kontekście API?
    # oznacza to stronnicowanie informacji wracajacych z api
# 12. Jak pobrać dane z kilku stron API z paginacją?
        #result = []
    #   while(True):
        #response = requests.get(url,params={'page':page})
        #data = response.json()
        #if not data:
            #break
        #result.append()
        #page += 1
# 13. Jak działa API wymiany walut, np. Exchange Rates API?
    # jak kazde inne api, wykonujesz zapytanie dostaniesz informacjie
# 14. Co to jest klucz API (API key) i po co się go używa?
    # jest on przypisany do kazdego konta na stronie dla danego api, jest to jak haslo umozliwajace okreslona ilosc zapytan
# 15. Jakie dane można pozyskać z API iTunes?
        # o utworach muzycznych itp itd
# 16. Jakie jest ryzyko nie prawidłowego parsowania danych JSON?
    #Jeśli struktura JSON różni się od oczekiwanej (np. brak klucza), spowoduje to KeyError lub TypeError
# 17. Jak sprawdzić liczbę wyników w odpowiedzi API?
    # jak w zadanie 12 tylko na koniec dodac print(len(result))
# 18. Czy można filtrować dane bezpośrednio w zapytaniu GET?
    #tak, poprzez parametry
# 19. Jakie narzędzie API udostępnia dane o kursach walut?
    # exchange rates
# 20. W jakiej sytuacji API może zwrócić zbyt dużo danych?
    # jak jest zbyt ogolne zapytanie
# 21. Dlaczego warto logować błędy przy pracy z API?
    # zeby wiedziec czy zapytania byly poprawne
# 22. Jak poprawnie przechowywać klucze API w projektach?
    # W pliku .env 
# 23. Co zrobić, jeśli API ogranicza liczbę zapytań na minutę?
    #WYKONYWac mniejsza ilosc zapytan
# 24. W jaki sposób można przetestować działanie API bez kodowania?
    # w przegladarce, lub postmancurl
# 25. Co może zawierać nagłówek (headers) w zapytaniu do API?
    #Np. nagłówek Content-Type: application/json, Authorization: Bearer <token>