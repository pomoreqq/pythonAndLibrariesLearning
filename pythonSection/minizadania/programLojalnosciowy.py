klienci = [
    {"id": 1, "name": "Anna", "points": 120},
    {"id": 2, "name": "Tomek", "points": 90},
    {"id": 3, "name": "Kasia", "points": 300},
    {"id": 4, "name": "Piotr", "points": 50}
]


def awansujKielntow(dane):
    for i in dane:
        if i.get('points') > 100:
            i['VIP'] = True
        else:
            i['VIP'] = False
    return dane



klienci = awansujKielntow(klienci)


def nagradzajKlientow(dane):
    for i in dane:
        if i.get('VIP') == True:
            i['points'] += 50
        else:
            i['points'] += 20
    return dane


klienci = nagradzajKlientow(klienci)
# print(klienci)

def wypiszKlientow(dane):
    for i in dane:
        if i.get('VIP') == True:
            print(f"{i['name']} (VIP): {i['points']} pkt")
        else:
            print(f"{i['name']}: {i['points']} pkt")


print(wypiszKlientow(klienci))