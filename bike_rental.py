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
            json.dump(data, file)

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

          
                print("\nAktywne wynajmy:\n")
                for rental in data:
                    print(f"Imię klienta: {rental['customer_name']}")
                    print(f"Długość wynajmu: {rental['rental_duration']} godzin")
                    print(f"Koszt: {calculate_cost(rental['rental_duration'])} PLN")
                    print("-_" * 25)
               
        except ValueError:
            print(f"Plik {filename} nie istnieje.")

def cancel_rental(customer_name):
    folder_path = "data/"
    filename = os.path.join(folder_path, "rentals.json")

    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
            rental_to_remove = None
            for rental in data:
                if rental['customer_name'].lower() == customer_name.lower():  # Porównanie ignorując wielkość liter
                    rental_to_remove = rental
                    break
            if rental_to_remove:
                data.remove(rental_to_remove)
            print(f"Wynajem klienta {customer_name} został anulowany")
            with open(filename, "w") as file:
                    json.dump(data, file)
        except ValueError:
            print("Plik nie istnieje")

def generate_daily_report():
    folder_path = "data/"
    filename = os.path.join(folder_path, "rentals.json")

    if os.path.exists(filename):
        try:
            # Wczytanie danych z pliku wynajmów
            with open(filename, "r") as file:
                data = json.load(file)

            # Pobranie dzisiejszej daty
            today_date = datetime.datetime.now().strftime("%Y-%m-%d")

            # Tworzenie nazwy pliku dla raportu dziennego
            daily_report_filename = os.path.join(folder_path, f"daily_report_{today_date}.json")

            # Zapisanie danych do pliku raportu
            with open(daily_report_filename, "w") as report_file:
                json.dump(data, report_file, indent=4)

            print(f"Raport dzienny pomyślnie zapisano w pliku {daily_report_filename}.")
        except ValueError:
            print(f"Plik {filename} zawiera błędny format lub jest pusty.")
    else:
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
        elif option == "2":
            load_rentals()
        elif option == "3":
            customer_name=input("Podaj nazwę klienta: ")
            cancel_rental(customer_name)
        elif option == "4":
            generate_daily_report()
        elif option == "5":
            print("Zakończenie programu")
            break