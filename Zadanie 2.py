#Jaki sport jest najbardziej i namniej popularny wśród klientów?

import pandas as pd

#wczytanie danych z pliku csv
sports = pd.read_csv('sports.csv')
#czyszczenie zbędnej kolumny
sports.rename(columns = {'Unnamed: 0':'id'}, inplace = True)
sports.drop('id', inplace=True, axis=1)

#zliczenie ile razy dany sport występuje w kolumnie
value_counts = sports['sport'].value_counts()
#znalezienie liczb najczęściej i najżadziej uprawianym sporcie
max_l = value_counts.max()
min_l = value_counts.min()

#znalezienie nazw sportów najczęsciej i najżadziej uprawianych sportów
max = sports['sport'].value_counts().idxmax()
min = sports['sport'].value_counts().idxmin()

#wydrukowanie odpowiedzi
print(f'Najczęściej uprawianym sportem przez naszych klientów jest {max}, czyli aż {max_l} osób uprawia {max}.')
print(f'Najżadziej uprawianym sportem przez naszych klientów jest {min}, czyli {min_l} uprawia {min}.')




