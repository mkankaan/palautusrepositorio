from abc import ABC, abstractmethod
from tuomari import Tuomari

class KiviPaperiSakset(ABC):
    def __init__(self):
        super().__init__()
        self._tuomari = Tuomari()

    @abstractmethod
    def pelaa(self):
        pass

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    @abstractmethod
    def _toisen_siirto(self, ensimmaisen_siirto):
        pass

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
