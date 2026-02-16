from datetime import datetime
from zoneinfo import ZoneInfo
from klient import Klient

class Zamowienie:
    def __init__(self,klient,koszyk = []):
        self.klient = klient
        self.koszyk = koszyk
        self.data = datetime.now(ZoneInfo("Europe/Warsaw"))

    def dodaj_produkt(self,produkt):
        self.produkt = produkt
        if produkt.czy_tylko_dla_pelnoletnich == True:
            if self.klient.czy_pelnoletni() == True:
                self.koszyk.append(produkt)
        else:
            self.koszyk.append(produkt)

    def drukuj_zamowienie(self):
        return self.koszyk








