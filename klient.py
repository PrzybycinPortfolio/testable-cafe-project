from datetime import datetime

class Klient:
    def __init__(self, id, imie, data_urodzenia):
        self.id = id
        self.imie = imie
        # data_urodzenia jako string w formacie "YYYY-MM-DD"
        # lub jako obiekt datetime.date
        if isinstance(data_urodzenia, str):
            self.data_urodzenia = datetime.strptime(data_urodzenia, "%Y-%m-%d").date()
        else:
            self.data_urodzenia = data_urodzenia

    def czy_pelnoletni(self):
        today = datetime.today().date()
        wiek = today.year - self.data_urodzenia.year - (
            (today.month, today.day) < (self.data_urodzenia.month, self.data_urodzenia.day)
        )
        return wiek >= 18

    def __str__(self):
        status = "PEŁNOLETNI" if self.czy_pelnoletni() else "NIEPEŁNOLETNI"
        return f"ID: {self.id}, Imię: {self.imie}, Data urodzenia: {self.data_urodzenia}, Status: {status}"
