


def wczytajZamowienie():
    while(True):
        print('podaj informacje o zamowieniu w formacie: produkt,ilosc,cena')
        dane = input()
        splittedDane = dane.split(',')

        if len(splittedDane) != 3:
            print('dane sie nie zgadzaja, za malo lub za duzo informacji')
            continue
        
        produkt = splittedDane[0].strip()

        try:
            ilosc = int(splittedDane[1].strip())
        except ValueError:
            print('ilosc musi byc liczba calkowita')
            continue
        try:
            cena = float(splittedDane[2].strip())
        except ValueError:
            print('ilosc musi byc liczba zmiennoprzecinkowa')
            continue
        return {
            'produkt': produkt,
            'ilosc':ilosc,
            'cena':cena
        }
    

print(wczytajZamowienie())

