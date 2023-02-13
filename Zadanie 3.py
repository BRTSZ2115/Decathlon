#Ilu klientów uprawia więcej niż 2 sporty?

import pandas as pd

#wczytanie danych z pliku CSV
sports = pd.read_csv('sports.csv')
#czyszczenie zbędnej kolumny
sports.rename(columns = {'Unnamed: 0':'id'}, inplace = True)
sports.drop('id', inplace=True, axis=1)

#zliczenie ile razy występuje customer_id czyli ile różnych sportów uprawia osoba
value_counts = sports['customer_id'].value_counts()

#utworzenie dataframe z customer_id które występują więcej niż 2 razy
duplicates = value_counts[value_counts > 2]

#zliczenie ile jest wierszy w dataframe z osobami które uprawiają więcej niż 2 sporty
result  = len(duplicates)

#wyświetlenie odpowiedzi
print(f'{result} klientów uprawia więcej niż 2 sporty.')



