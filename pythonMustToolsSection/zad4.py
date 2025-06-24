clients = [
    {'name': 'Alice', 'orders': [120, 75, 300]},
    {'name': 'Bob', 'orders': []},
    {'name': 'Charlie', 'orders': [10, 25]},
    {'name': 'Diana', 'orders': [500, 5]}
]


def high_value_clients(clients,threshold):
    setClients = set()
    for i in clients:
        for j in i['orders']:
            if j > threshold:
                setClients.add(i['name'])
    return setClients


print(high_value_clients(clients,100))
# def high_value_clients(clients, threshold):
#     result = []
#     for client in clients:
#         for order in client['orders']:
#             if order > threshold:
#                 if client['name'] not in result:  # zapobiegamy duplikatom
#                     result.append(client['name'])
#                 break  # już znaleźliśmy 1 zamówienie > threshold
#     return result
