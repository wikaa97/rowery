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
    filename="rentals.json"
    try:
        # Sprawdzenie, czy plik istnieje
        if os.path.exists(filename):
            # Jeśli plik istnieje, wczytaj istniejące dane
            with open(filename, "r") as file:
                data = json.load(file)
        else:
            # Jeśli plik nie istnieje, rozpocznij od pustej listy
            data = []

        # Dodanie nowego wynajmu do danych
        data.append(rental)

        # Zapisanie zaktualizowanych danych do pliku
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        print(f"Wynajem zapisano pomyślnie w pliku {filename}.")
    except Exception as blad:
        print(f"Wystąpił błąd podczas zapisu: {blad}")


rent_bike