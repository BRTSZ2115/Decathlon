#Jaka jest średnia wartość zamówienia?

import pandas as pd

#wczytanie danych z pliku csv
orders = pd.read_csv('orders.csv')
#czyszczenie zbędnej kolumny
orders.rename(columns = {'Unnamed: 0':'id'}, inplace = True)
orders.drop('id', inplace=True, axis=1)

#poprawienie formatowania i wyczyszczenie wartości ujemnych
orders['value'] = orders['value'].abs()
#Zamówienia na które w polsce nie potrzebny jest przetarg są do 130tyś, dlatego też usuwamy wartości które śą ponad 130tyś
#zakładamy że to błędna wartość i nie wpłynie na średnią wartość
orders2 = orders[orders['value'] < 130000 ]


#zliczenie średnią z zamówieniami gdzie zostawiliśmy również wartości ponad 130 tyś
mean = orders['value'].mean()
mean = round(mean, 2)

#zliczamy średnią z zamówień poniżej 130 tyś
mean2 = orders2['value'].mean()
mean2 = round(mean2, 2)

#wypisanie odpowiedzi
print(f'Średnia wartość zamówienia przy założeniu że istnieją również gigantyczne zamówienia hurtowe to {mean} zł')
print(f'Średnia wartość zamówienia detalicznego zakładając że zamówienie detaliczne kończy się na 130 tyś zł, to {mean2} zł')