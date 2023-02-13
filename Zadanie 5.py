#Jaka jest średnia wartość zamówienia klientów uprawiających jeździectwo
#sporty, zamowienia, baza klientów

import pandas as pd

#import plików csv
customer_orders = pd.read_csv('customer_orders.csv')
orders = pd.read_csv('orders.csv')
sports = pd.read_csv('sports.csv')

#czyszczenie zbędnej kolumny
sports = pd.read_csv('sports.csv', encoding='utf-8')
sports.rename(columns = {'Unnamed: 0':'id'}, inplace = True)
sports.drop('id', inplace=True, axis=1)

orders = pd.read_csv('orders.csv', encoding='utf-8')
orders.rename(columns = {'Unnamed: 0':'id'}, inplace = True)
orders.drop('id', inplace=True, axis=1)

customer_orders = pd.read_csv('customer_orders.csv', encoding='utf-8')
customer_orders.rename(columns = {'Unnamed: 0':'id'}, inplace = True)
customer_orders.drop('id', inplace=True, axis=1)

#czyszczenie z wartości ujemnych oraz wartości ponad 130tyś
orders['value'] = orders['value'].abs()
orders = orders[orders['value'] < 130000 ]

#utworzenie dataframe tylko z wierszami z wartością jeździectwo w kolumnie sport
sports = sports[sports['sport'] == 'jeYdziectwo' ]
#połączenie kolumn aby móc porównać wartości zamówień klientów którzy uprawiają jeździectwo
result = pd.merge(sports, customer_orders, on='customer_id')
result2 = pd.merge(result, orders, on='order_id')

#wyliczenie średniej zamówień klientów uprawiających jeździectwo
mean = result2['value'].mean()
mean = round(mean, 2)

print(f'Średnia wartość zamówień klientów uprawiających jeździectwo to {mean} zł')
