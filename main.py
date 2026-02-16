from produkt import Produkt
from klient import Klient
from zamowienie import Zamowienie

# Lista produktów: (nazwa, cena, czy_tylko_dla_pelnoletnich)
produkty_info = [
    # Kawy
    ("Espresso", 8.0, False),
    ("Cappuccino", 12.0, False),
    ("Latte", 14.0, False),
    # Desery
    ("Ciasto czekoladowe", 12.5, False),
    ("Croissant", 9.0, False),
    # Alkohol
    ("Piwo jasne", 12.0, True),
    ("Wino czerwone", 25.0, True),
    ("Vodka 50ml", 28.0, True),
]

# Tworzymy menu
menu = []
for nazwa, cena, czy_18plus in produkty_info:
    menu.append(Produkt(nazwa, cena, czy_tylko_dla_pelnoletnich=czy_18plus))

print("=== DOSTĘPNE MENU ===")
for p in menu:
    print(p)
print("\n")

