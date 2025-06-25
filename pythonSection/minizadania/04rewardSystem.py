
# Task: Classify and reward VIP clients
# You are given a list of clients with their names and point balances.
# 1. Classify each client as VIP if they have more than 100 points.
# 2. VIP clients receive +50 points, non-VIPs receive +20 points.
# 3. Print a summary showing each client's name, updated points, and VIP status (if applicable).


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