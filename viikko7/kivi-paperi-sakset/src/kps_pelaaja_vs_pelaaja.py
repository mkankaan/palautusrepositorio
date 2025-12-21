from kps import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def __init__(self):
        super().__init__()

    def _toisen_siirto(self):
        return input("Toisen pelaajan siirto: ")
