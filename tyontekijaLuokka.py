class Tyontekija:
    ika = 0
    nimi = ""
    tyoKokemus = 0
    palkka = 1.00
    osasto = ""

    def __init__ (self, nimi, ikavuodet, palkkasumma, osasto, kokemus):
        self.nimi = nimi
        self.ika = ikavuodet
        self.palkka = palkkasumma
        self.osasto = osasto
        self.tyoKokemus = kokemus

