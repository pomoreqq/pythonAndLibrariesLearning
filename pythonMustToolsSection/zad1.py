clients = [
    {'name': 'Anna', 'points': 120},
    {'name': 'Bartek', 'points': 80},
    {'name': 'Celina', 'points': 150},
    {'name': 'Daniel', 'points': 95}
]


listComp = [x['name'].lower() for x in clients if x['points'] > 100]
print(listComp)