from tuomari import Tuomari
from tekoaly import Tekoaly
from kps import KiviPaperiSakset

class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        super().__init__()
        self._tekoaly = Tekoaly()

    def pelaa(self):
        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self._tuomari)

            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = self._toisen_siirto(ekan_siirto)

            print(f"Tietokone valitsi: {tokan_siirto}")

        print("Kiitos!")
        print(self._tuomari)

    def _toisen_siirto(self, ensimmaisen_siirto):
        return self._tekoaly.anna_siirto()
    
    def _pelaa_kierros(self):
        pass
