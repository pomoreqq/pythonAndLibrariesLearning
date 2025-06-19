#kalkulator danych osobowuch

# def kalkulatorDanychOsobowych(imie,nazwisko,wiek):
#     wiekObliczony = 2025 - wiek
#     if wiekObliczony < 18:
#         print('ostrzezenie')
        
#         print(f"{imie} {nazwisko} ma {wiekObliczony} lat")
#     else:
#         print(f"{imie} {nazwisko} ma {wiekObliczony} lat")

#2. System punktacji klientów

# clients = [
#     {"name": "Anna", "score": 120},
#     {"name": "Piotr", "score": 80},
#     {"name": "Zofia", "score": 200}
# ]


# def moreThan100(listOfDictonaries):
#     for i in listOfDictonaries:
#         if i['score'] > 100:
#             print(i['name'])
#             i['VIP'] = True
    
# moreThan100(clients)
# print(clients)

# def printWithVip(listOfDictonaries):
#     for i in listOfDictonaries:
#         if i.get('VIP'):
#             print(i['name'], "('VIP') :", i['score'])

# printWithVip(clients)



#3

products = {
    "kawa": 12,
    "herbata": 8,
    "woda": 5
}

def funkcja():
    print('Podaj nazwe produktu: kawa,herbata,woda')
    produkt = str(input())
    if produkt not in products:
        return 'Error nie ma produktu w ofercie'
    print('ile sztuk: ')
    ilosc = int(input())

    calkowityKoszt = products[produkt] * ilosc
    return f"calkowity koszt {calkowityKoszt}"

print(funkcja())