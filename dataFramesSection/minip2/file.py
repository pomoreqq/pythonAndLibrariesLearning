import pandas as pd

data = pd.read_csv('dataFramesSection/minip2/Zam_wienia_Online__df_orders_.csv')


# 1. 📈 Która kategoria przyniosła największy łączny przychód? // clothing wygenerowalo najwiekszy zysk

data['revenue'] = data['quantity'] * data['price_per_unit']


aggByCategory = data.groupby('category').agg(
    reevenueByCategory = ('revenue','sum')
)

revenueMax = aggByCategory.idxmax()

# 2. 📉 Który użytkownik wydał najmniej łącznie (suma z wszystkich zamówień)?
aggByUser = data.groupby('user_id')['revenue'].sum()
minUser = aggByUser.idxmin()


# 3. 🧮 Ile średnio produktów (suma quantity) zamawiają użytkownicy z kategorii „electronics” /362
electronics = data[data['category'] == 'electronics']
avg_per_user = electronics.groupby('user_id')['quantity'].sum().mean()


# 4. 🔄 Który dzień miał najwyższy średni przychód z zamówienia? 2023-01-16


groupByOrderDate = data['revenue'].groupby(data['order_date']).apply(lambda s: s.mean())

maxDay = groupByOrderDate.idxmax()
print(maxDay)

# 5. 🎯 Dla każdego użytkownika policz liczbę dni, w które złożył zamówienie

active_days = data.groupby('user_id')['order_date'].nunique()
