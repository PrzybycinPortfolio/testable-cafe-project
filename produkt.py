class Produkt:
    def __init__(self, id, nazwa, cena, czy_tylko_dla_pelnoletnich=False):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena
        self.czy_tylko_dla_pelnoletnich = czy_tylko_dla_pelnoletnich

    def __str__(self):
        return (f"ID: {self.id} {self.nazwa} - {self.cena} zł" +
                (" TYLKO DLA PEŁNOLETNICH" if self.czy_tylko_dla_pelnoletnich else ""))
