from tuomari import Tuomari
from tekoaly import Tekoaly
from kps import KiviPaperiSakset

class KPSTekoaly(KiviPaperiSakset):
    def pelaa(self):
        tuomari = Tuomari()
        self._tekoaly = Tekoaly()

        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = self._tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = self._toisen_siirto(ekan_siirto)

            print(f"Tietokone valitsi: {tokan_siirto}")

        print("Kiitos!")
        print(tuomari)

    def _toisen_siirto(self, ensimmaisen_siirto):
        return self._tekoaly.anna_siirto()
