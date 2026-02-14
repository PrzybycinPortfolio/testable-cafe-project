from produkt import Produkt

# Lista produktów: (nazwa, cena)
produkty_info = [
    # Kawy
    ("Espresso", 8, False),
    ("Cappuccino", 12, False),
    ("Latte", 14, False),
    ("Americano", 10, False),
    ("Mocha", 16, False),
    # Herbaty
    ("Herbata zielona", 6, False),
    ("Herbata czarna", 6, False),
    ("Herbata owocowa", 7, False),
    # Desery i przekąski
    ("Ciasto czekoladowe", 12, False),
    ("Croissant", 9, False),
    ("Kanapka z szynką", 15, False),
    ("Bagietka z serem", 13, False),
    # Napoje alkoholowe
    ("Piwo jasne", 12, True),
    ("Piwo ciemne", 14, True),
    ("Wino czerwone", 25, True),
    ("Wino białe", 22, True),
    ("Whisky 50ml", 30, True),
    ("Vodka 50ml", 28, True),
]

# Tworzymy menu jako listę obiektów Produkt
menu = []
for idx, (nazwa, cena,czy_tylko_dla_pelnoletnich) in enumerate(produkty_info, start=1):
    menu.append(Produkt(idx, nazwa, cena,czy_tylko_dla_pelnoletnich))

# Wyświetlamy menu
print("=== MENU KAWIARNI ===")
for produkt in menu:
    print(produkt)
