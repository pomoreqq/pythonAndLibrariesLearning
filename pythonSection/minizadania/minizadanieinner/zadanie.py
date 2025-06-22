
produkty = open('pythonSection/minizadania/minizadanieinner/1.txt', mode='r')

zamowienia = open('pythonSection/minizadania/minizadanieinner/2.txt', mode='r')


produktyD = dict()

for i in produkty:
    splittedProdukty = i.strip().split(';')
    productCode,productType,price = splittedProdukty

    if productCode not in produktyD:
        produktyD[productCode] = dict()
    
    produktyD[productCode]['name'] = productType
    produktyD[productCode]['price'] = price


print(produktyD)
laczneZamowienia = dict()
for i in zamowienia:
    splittedZamowienie = i.strip().split(';')
    imie,code,quantity = splittedZamowienie
    
    suma = int(produktyD[code]['price']) * int(quantity)
    if imie not in laczneZamowienia:
        laczneZamowienia[imie] = suma
    else:
        laczneZamowienia[imie] += suma
    print(f'{imie} - {suma} - zl')
    

print(laczneZamowienia) 
