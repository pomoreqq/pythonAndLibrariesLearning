import requests
# Zadanie 1: Paginacja i zbieranie danych z wielu stron
# Pobierz dane z API z parametrem page=X, aż do pustej strony.
# Połącz wszystkie dane w jedną listę i wypisz ich liczbę.
results = []
page = 1
url ='dummyUrl'
while(True):
    response = requests.get(url,params={'page':page})
    
    data = response.json()['results']
    if not data:
        
        break
    results.extend(data)
    page += 1
    print(f'zebramo {len(results)} rekordow')