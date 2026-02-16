from produkt import Produkt
from klient import Klient
from zamowienie import Zamowienie

# 1. Definicja bazy produktów
produkty_info = [
    ("Espresso", 8.0, False),
    ("Cappuccino", 12.0, False),
    ("Latte", 14.0, False),
    ("Ciasto czekoladowe", 12.5, False),
    ("Croissant", 9.0, False),
    ("Piwo jasne", 12.0, True),
    ("Wino czerwone", 25.0, True),
    ("Vodka 50ml", 28.0, True),
]

# Tworzenie obiektów menu na podstawie listy
menu = [Produkt(n, c, adult) for n, c, adult in produkty_info]


def uruchom_cli():
    print("=== SYSTEM KAWIARNI v2.0 ===")

    # 2. Rejestracja klienta z obsługą błędów
    klient = None
    while klient is None:
        imie = input("Podaj imię klienta: ")
        data_ur = input("Podaj datę urodzenia (RRRR-MM-DD): ")
        try:
            klient = Klient(imie, data_ur)
            print(f"\nZalogowano pomyślnie!")
            print(klient)  # Wyświetla status pełnoletności
        except ValueError as e:
            print(f"❌ BŁĄD: {e}. Spróbuj ponownie.")

    # Inicjalizacja zamówienia
    zamowienie = Zamowienie(klient)

    # 3. Pętla wyboru produktów
    while True:
        print("\n" + "=" * 30)
        print(f"{'ID':<4} | {'NAZWA':<20} | {'CENA'}")
        print("-" * 30)
        for p in menu:
            print(p)  # Wykorzystuje __str__ z klasy Produkt

        wybor = input("\nWpisz ID produktu, aby go dodać (lub 'ok' by skończyć): ").strip().lower()

        if wybor == 'ok':
            break

        try:
            id_wyboru = int(wybor)
            # Szukanie produktu w menu po ID
            wybrany_produkt = next((p for p in menu if p.id == id_wyboru), None)

            if wybrany_produkt:
                # Metoda dodaj_produkt sama sprawdzi wiek i zliczy sztuki
                zamowienie.dodaj_produkt(wybrany_produkt)
            else:
                print("❌ Nie ma produktu o takim ID!")
        except ValueError:
            print("❌ Błąd! Podaj numer ID lub wpisz 'ok'.")

    # 4. Finałowy paragon
    if zamowienie.koszyk:
        zamowienie.drukuj_podsumowanie()
    else:
        print("\nKoszyk jest pusty. Do widzenia!")


if __name__ == "__main__":
    uruchom_cli()