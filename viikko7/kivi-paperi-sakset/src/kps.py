from abc import ABC, abstractmethod
from tuomari import Tuomari

class KiviPaperiSakset(ABC):
    def __init__(self):
        super().__init__()
        self._tuomari = Tuomari()

    def pelaa(self):
        self._ekan_siirto = self._ensimmaisen_siirto()
        self._tokan_siirto = self._toisen_siirto()

        while self._onko_ok_siirto(self._ekan_siirto) and self._onko_ok_siirto(self._tokan_siirto):
            self._pelaa_kierros(self._ekan_siirto, self._tokan_siirto)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")
    
    def _pelaa_kierros(self, ekan_siirto, tokan_siirto):
        self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
        print(self._tuomari)

        self._ekan_siirto = self._ensimmaisen_siirto()
        self._tokan_siirto = self._toisen_siirto()

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    @abstractmethod
    def _toisen_siirto(self):
        pass

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
