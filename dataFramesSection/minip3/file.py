import pandas as pd


data = pd.read_csv('dataFramesSection/minip3/MiniProjekt_DF.csv')

# 🔹 1. Aktywność użytkowników
# Którzy użytkownicy złożyli najwięcej zamówień? (top 5)/ uzytkownicy 1061,1032, 1001,1098,1089

# Ilu użytkowników złożyło zamówienia w co najmniej 5 różnych dniach? 26 userow

# Którzy użytkownicy mają najwyższy średni przychód na zamówienie?1089,1053,1026,1061,1091

groupedByUser = data.groupby('user_id').agg(
    sumOfOrders = ('order_id','count'),
    uniqueDaysOfOrders = ('order_date','nunique'),
    meanRevenue = ('revenue',lambda s: s.sum().mean())
)

groupedByUser = groupedByUser.sort_values(by='sumOfOrders',ascending=False)

topFiveUsers = groupedByUser['sumOfOrders'].head()


usersWithAtleastFiveDaysOfOrders = len(groupedByUser[groupedByUser['uniqueDaysOfOrders'] > 5])

topFiveUsersHighestSumMean = groupedByUser['meanRevenue'].sort_values(ascending=False).head()
print(topFiveUsersHighestSumMean)



# 🔹 2. Analiza produktów i kategorii
# Który produkt jest najczęściej zamawiany w każdej kategorii?
groupedByCategoryAndProduct = data.groupby(['category','product'])['quantity'].sum()
maxProductByCategory = groupedByCategoryAndProduct.groupby('category').idxmax()

# Dla każdej kategorii: jaki jest średni przychód na zamówienie?
test = data.groupby(['category','order_id'])['revenue'].mean()
print(test)
# Czy są produkty, które nigdy nie były zamówione więcej niż 2 sztuki naraz?
