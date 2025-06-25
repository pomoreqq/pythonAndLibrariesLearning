
# Task: Collect and summarize user orders
# Prompt the user repeatedly to input orders in the format: name, product, quantity.
# Stop when the user types 'stop'.
# For each correct entry, save the order in a list of dictionaries.
# After exiting, summarize:
#   - the number of orders entered,
#   - a breakdown of products ordered per user.
# Invalid lines should be skipped with a warning message.

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