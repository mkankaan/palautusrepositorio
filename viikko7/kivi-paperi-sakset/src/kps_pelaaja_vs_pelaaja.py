from tuomari import Tuomari
from kps import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = input("Toisen pelaajan siirto: ")

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _toisen_siirto(self, ensimmaisen_siirto):
        return input("Toisen pelaajan siirto: ")
