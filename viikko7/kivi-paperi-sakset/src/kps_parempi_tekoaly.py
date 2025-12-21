from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from kps import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        super().__init__()
        self._tekoaly = TekoalyParannettu(10)

    def _pelaa_kierros(self, ekan_siirto, tokan_siirto):
        super()._pelaa_kierros(ekan_siirto, tokan_siirto)
        self._tekoaly.aseta_siirto(ekan_siirto)

    def _toisen_siirto(self):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto
