class Produkt:
    _max_produkt_id = 0  # Konwencja: _ zmienna "prywatna" dla klasy

    def __init__(self, nazwa: str, cena: float, czy_tylko_dla_pelnoletnich: bool = False):
        self.id = Produkt._max_produkt_id
        Produkt._max_produkt_id += 1
        self.nazwa = nazwa
        self.cena = cena
        self.czy_tylko_dla_pelnoletnich = czy_tylko_dla_pelnoletnich

    def __str__(self) -> str:
        info = f"[{self.id}] {self.nazwa:<20} | {self.cena:.2f} PLN"
        if self.czy_tylko_dla_pelnoletnich:
            info += " (18+)"
        return info

    def __repr__(self):
        return f"<Produkt(id={self.id}, nazwa='{self.nazwa}')>"