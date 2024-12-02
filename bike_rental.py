import json, datetime, smtplib

def calculate_cost(rental_duration):
    
    if (rental_duration == 1):
        cost=10
    else:
        cost=10+5*(rental_duration-1) 
    return cost


rental_duration=int(input("ile godzin: "))

print(calculate_cost(rental_duration))

def rentbike(customer_name, rental_duration): #dodaje wynajem roweru



    return