produkty = [
    {"name": "Monitor", "price": 800, "available": True},
    {"name": "Laptop", "price": 3000, "available": False},
    {"name": "Myszka", "price": 100, "available": True},
    {"name": "Klawiatura", "price": 150, "available": True},
    {"name": "Kamera", "price": 450, "available": False}
]



sortedList = sorted(produkty,key= lambda d: d['price'])

available = [p for p in produkty if p['available'] == True]
sortedDostepne = sorted(available, key=lambda d: d["price"], reverse=True) 


for i in produkty:
    if i.get('available') == True:
        print(f"{i['name']} - {i['price']} - Dostepny")
    else:
        print(f"{i['name']} - {i['price']} - nieDostepny")