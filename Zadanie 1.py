#Jaki odsetek klientów odbiera swoje zamówienia
#pod innym kodem pocztowym niż mieszka?

import pandas as pd

#wczytanie danych z pliku csv
customers_zip = pd.read_csv('customers_zip.csv')
#czyszczenie zbędnej kolumny
customers_zip.rename(columns = {'Unnamed: 0':'id'}, inplace = True)
customers_zip.drop('id', inplace=True, axis=1)

delivery_zip = pd.read_csv('delivery_zip.csv')
delivery_zip.rename(columns = {'Unnamed: 0':'id'}, inplace = True)
delivery_zip.drop('id', inplace=True, axis=1)

#funkcja liczenia procentów
def calculate_percentage(part, whole):
    return round(((part / whole) * 100), 2)

#wyciągnięcie z pliku wierszy z pustą wartością w miejscu kodu pocztowego
nulls = delivery_zip[delivery_zip['zip_del'].isnull()]

#połączenie dwóch DataFrame z kodem pocztowym domowym i dostawy
result = pd.merge(customers_zip, delivery_zip, on='customer_id')

#utworzenie nowego data frame z którym mamy powtarzające się wartości w obu dataframe, domowym i dostawy
the_same = result[result['zip_cust'] == result['zip_del']]

#wyczyszczenie duplikatów
the_same.drop_duplicates()
nulls.drop_duplicates()

#zakładając że niewypełniony kod pocztowy w adresie dostawy oznacza że wysyłamy na adres domy
#zliczenie ilości wierszy gdzie kod pocztowy dostawy jest pusty oraz powtarza się w kodzie pocztowym domowym
the_same_quantity = len(nulls) + len(the_same)

#obliczamy ile jest w sumie adresów
whole_quantity = len(delivery_zip)

#obliczamy róznicę
differen_quantity = whole_quantity - the_same_quantity

#obliczamy procent osób kóre mają dostawę na inny adres niż domowy
procentage = calculate_percentage(differen_quantity, whole_quantity)

#wypisujemy wynik
print(f'{procentage}% ludzi odbiera zamówienia pod innym adresem niż mieszka. ')



