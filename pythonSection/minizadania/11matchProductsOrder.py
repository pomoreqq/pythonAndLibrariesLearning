# Task: Process product orders from two input files
# File 1 (`1.txt`) contains product data in the format: product_code;product_name;price
# File 2 (`2.txt`) contains orders in the format: customer_name;product_code;quantity
#
# 1. Read all products into a dictionary mapping product codes to name and price.
# 2. Read all orders and match product codes with their price from the product dictionary.
# 3. For each order, calculate the total value and print it with the customer's name.
# 4. In the end, print a summary dictionary showing total spending per customer.

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
