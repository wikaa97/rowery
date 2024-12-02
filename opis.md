# System wynajmu rowerów
```
Aplikacja służy do zapisów wynajmu rowerów przez klientów.
```

## Wymagane biblioteki
-`json` 

-`datetime`

-`os`


-**Struktura plików**:
```
bike_rental/
├── bike_rental.py
├── data/
│   └── rentals.json
└── └──daily_reports/
```

## Funkcje:
1. **Funkcja rent_bike(customer_name, rental_duration)**
   - Funkcja wywołuje `calculate_cost()` by obliczyć koszta, a następnie zapisuje dane klienta do `save_rental`.
```py
def rent_bike(customer_name, rental_duration)

rent_bike("Jan Kowalski", 5)
```

2. **Funkcja calculate_cost(rental_duration)**
   - Wylicza koszt wynajmu.
   - Zasady: pierwsza godzina kosztuje 10 zł, każda następna to 5 zł.

```py
def calculate_cost(rental_duration)

calculate_cost(5)
```
3. **Funkcja save_rental(rental)**
    - Funkcja zapisuje wynajem do pliku `rentals.json`.
    - Sprawdza, czy plik `rentals.json` istnieje, jeśli nie to go tworzy.
    - Używa funkcji `json.dump()` do zapisu danych w pliku.
```py
def save_rental(rental)
```

4. **Funkcja load_rentals()**
    - Wczytuje dane z pliku `rentals.json` i wyświetla zapisane wynajmy.
```py
def load rentals()
```
```
Aktywne wynajmy:

Imię klienta: Jan Kowalski
Długość wynajmu: 5 godzin
Koszt: 30 PLN
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
5. **Funkcja cancel_rental(customer_name)**
    - Funkcja wczytuje dane z pliku `rentals.json` i służy do usunięca odpowiednio rekordu ,a następnie zapisania zmian.
```py
def cancel_rental(customer_name)

cancel_rental("Jan Kowalski")
```

6. **Funkcja generate_daily_report()**
    - Służy do zapisania wynajmów do pliku `daily_report_<daily>.json` z uzyskaniem dzisiejszej daty.