import json
import datetime 
import smtplib 
import os

def calculate_cost(rental_duration):
    
    if (rental_duration == 1):
        cost=10
    else:
        cost=10+5*(rental_duration-1) 
    return cost


def rent_bike(customer_name, rental_duration): #dodaje wynajem roweru
    if rental_duration<=0:
        print("Wynajem musi być większy od zera")
    cost=calculate_cost(rental_duration)
    rental_details= {
    "customer_name": customer_name,
    "rental_duration": rental_duration,
    }
    save_rental(rental_details)


def save_rental(rental):
    folder_path = "data/"
    filename = os.path.join(folder_path, "rentals.json")
    
    # Upewnij się, że folder istnieje
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    try:
        # Jeśli plik nie istnieje, rozpocznij od pustej listy
        if not os.path.exists(filename):
            data = []
        else:
            # Jeśli plik istnieje, spróbuj wczytać dane
            try:
                with open(filename, "r") as file:
                    data = json.load(file)  # Wczytanie danych z pliku
            except json.JSONDecodeError:
                print(f"Plik {filename} jest pusty lub ma nieprawidłowy format. Inicjalizowanie pustej listy.")
                data = []  # Jeśli plik ma błędny format, ustaw pustą listę

        # Dodanie nowego wynajmu do danych
        data.append(rental)

        
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        print(f"Wynajem zapisano pomyślnie w pliku {filename}.")
    except Exception as blad:
        print(f"Wystąpił błąd podczas zapisu: {blad}")

def load_rentals():
    folder_path = "data/"
    filename = os.path.join(folder_path, "rentals.json")

    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)  # Wczytanie danych z pliku

            # Sprawdzenie, czy dane są listą
            if isinstance(data, list):
                if data:
                    print("\nAktywne wynajmy:\n")
                    for rental in data:
                        print(f"Imię klienta: {rental['customer_name']}")
                        print(f"Długość wynajmu: {rental['rental_duration']} godzin")
                        print(f"Koszt wynajmu: {calculate_cost(rental['rental_duration'])} PLN")
                        print("-" * 25)
                else:
                    print("Brak zapisanych wynajmów.")
            else:
                print("Błąd: Plik zawiera nieprawidłowy format danych.")
        except ValueError:
            print(f"Plik {filename} nie istnieje.")

if __name__ == "__main__":
    while True:
        print("\n1. Wynajmij rower")
        print("2. Wyświetl aktywne wynajmy")
        print("3. Anuluj wynajem")
        print("4. Generuj raport dzienny")
        print("5. Wyjdź")

        option = input("Wybierz opcje: ")
        if option == "1":
            customer_name=input("Podaj imię: ")
            try:
                rental_duration=int(input("Podaj długość wynajmu: "))
                rent_bike(customer_name,rental_duration)
            except ValueError:
                print("Podana liczba musi być liczbą całkowitą")
        elif option == "5":
            print("Zakończenie programu")
            break