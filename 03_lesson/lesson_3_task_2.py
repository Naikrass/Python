from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "SE2020", "+79992355587"),
    Smartphone("Xiaomi", "10", "+79125698453"),
    Smartphone("Honor", "Deluxe", "+79089089898"),
    Smartphone("Samsung", "Galaxy S4", "+79876543211"),
    Smartphone("Redmi", "Note", "+79505336569")
]
for smartphone in catalog:
    print(f"{smartphone.phone_brand} - {smartphone.phone_model}. "
          f"{smartphone.phone_number}")
