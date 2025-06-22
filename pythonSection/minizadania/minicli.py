


zamowienia = []
helpDict = dict()
def zamowienie():
    while(True):

        print("Podaj zamówienie (format: imię, produkt, ilość) lub 'stop' aby zakończyć:")
        data = input()
        if (data == 'stop'):
            print('petla zakonczona')
            print('Podsumowanie: \n Zamówienia:', len(zamowienia))
            for i in zamowienia:
                if i['user'] not in helpDict:
                    helpDict[i['user']] = list() 
                
                helpDict[i['user']].append({
                    'product': i['product'],
                    'quantity': i['quantity']
                })
            for user,orders in helpDict.items():
                print(f'{user}')
                for order in orders:
                      print(f"  - {order['product']} ({order['quantity']})")
            break
        
        dataSplitted = data.strip().split(',')
        if len(dataSplitted) != 3:
            print('Niewlasciwy formant zamowienia')
            continue
        imie,produkt,ilosc = dataSplitted
        ilosc = int(ilosc)
        zamowienia.append({'user': imie,'product': produkt,'quantity':ilosc})
        
    

zamowienie()
print(zamowienia[0]['user'])