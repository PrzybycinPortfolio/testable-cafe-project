from datetime import datetime


class Zamowienie:
    def __init__(self, klient):
        self.klient = klient
        # Słownik {Produkt: ilość} zamiast listy
        self.koszyk = {}
        self.data = datetime.now()

    def dodaj_produkt(self, produkt):
        # Logika sprawdzania pełnoletności
        if produkt.czy_tylko_dla_pelnoletnich and not self.klient.czy_pelnoletni():
            print(f"⚠️ Odmowa: {self.klient.imie} nie jest osobą pełnoletnią!")
            return

        # Jeśli produkt już jest w koszyku, zwiększamy ilość
        if produkt in self.koszyk:
            self.koszyk[produkt] += 1
        else:
            self.koszyk[produkt] = 1
        print(f"✅ Dodano: {produkt.nazwa} (Razem: {self.koszyk[produkt]})")

    def oblicz_sume(self):
        # Sumujemy: cena * ilość dla każdego przedmiotu
        return sum(p.cena * ilosc for p, ilosc in self.koszyk.items())

    def drukuj_podsumowanie(self):
        print(f"\n{'=' * 30}")
        print(f"PARAGON: {self.data.strftime('%Y-%m-%d %H:%M')}")
        print(f"Klient: {self.klient.imie}")
        print("-" * 30)

        for produkt, ilosc in self.koszyk.items():
            laczna_cena = produkt.cena * ilosc
            # Formatowanie: Nazwa x Ilość | Cena łączna
            print(f"{produkt.nazwa:<15} x{ilosc:>2} | {laczna_cena:>6.2f} PLN")

        print("-" * 30)
        print(f"SUMA: {self.oblicz_sume():>19.2f} PLN")
        print(f"{'=' * 30}")