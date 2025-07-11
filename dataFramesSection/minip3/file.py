import pandas as pd
import numpy as np

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




# 🔹 2. Analiza produktów i kategorii
# Który produkt jest najczęściej zamawiany w każdej kategorii?
groupedByCategoryAndProduct = data.groupby(['category','product'])['quantity'].sum()
maxProductByCategory = groupedByCategoryAndProduct.groupby('category').idxmax()
print(maxProductByCategory)
# Dla każdej kategorii: jaki jest średni przychód na zamówienie?
groupByCategory = data.groupby('category').agg(
    ordersCount = ('order_id','count'),
    sumOfOrders = ('revenue','sum')
)
groupByCategory['meanPerOrder'] = groupByCategory['sumOfOrders'] / groupByCategory['ordersCount']

# Czy są produtky, które nigdy nie były zamówione więcej niż 2 sztuki naraz?, nie ma takich
groupByProducts = data.groupby('product')['quantity'].max()
productsWithMax2 = groupByProducts[groupByProducts <= 2]
print(productsWithMax2)

# 🔹 3. Analiza przychodów i dni
# Jaka jest średnia i mediana dziennego przychodu? mediana dziennego przychodu to 132,6825, a srednia to 161,869
groupedByDay = data.groupby('order_date').agg(
    meanOfEveryDay = ('revenue','mean'),
    medianOfEveryDay = ('revenue','median')
)
medianOfSingleDay = groupedByDay['medianOfEveryDay'].median()
meanOfSingleDay = groupedByDay['meanOfEveryDay'].mean()

# Które dni mają przychód poniżej mediany i ile ich jest? 15 tych dni jest
daysBelowMedian = groupedByDay[groupedByDay['medianOfEveryDay'] < medianOfSingleDay]
lenOfDaysBelowMedian = len(daysBelowMedian)


# W którym dniu był największy skok przychodu względem poprzedniego dnia? miedzy dniem 2023-01-03 a 2023-01-4
groupedByOrdedWithRevenue = data.groupby('order_date')['revenue'].sum()
differ = np.diff(groupedByOrdedWithRevenue)
differAbs = np.abs(differ)
differMax = differAbs.max()
differMaxId = np.argmax(differAbs)
groupedByOrdedWithRevenue = groupedByOrdedWithRevenue.reset_index()
dayWithMax = groupedByOrdedWithRevenue.iloc[[differMaxId,differMaxId + 1]]
print(dayWithMax)