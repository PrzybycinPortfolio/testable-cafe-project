from datetime import datetime, date
from typing import Union


class Klient:
    _max_klient_id = 0

    def __init__(self, imie: str, data_urodzenia: Union[str, date]):
        self.id = Klient._max_klient_id
        Klient._max_klient_id += 1
        self.imie = imie

        # Obsługa daty jako string lub obiekt date
        if isinstance(data_urodzenia, str):
            try:
                self.data_urodzenia = datetime.strptime(data_urodzenia, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Format daty musi być YYYY-MM-DD")
        else:
            self.data_urodzenia = data_urodzenia

    def czy_pelnoletni(self) -> bool:
        today = date.today()
        # Obliczanie wieku z uwzględnieniem czy urodziny już były w tym roku
        wiek = today.year - self.data_urodzenia.year - (
                (today.month, today.day) < (self.data_urodzenia.month, self.data_urodzenia.day)
        )
        return wiek >= 18

    def __str__(self) -> str:
        status = "PEŁNOLETNI" if self.czy_pelnoletni() else "NIEPEŁNOLETNI"
        return f"Klient: {self.imie} (ID: {self.id}), Ur.: {self.data_urodzenia}, Status: {status}"