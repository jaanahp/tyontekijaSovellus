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
    
    def tulostaTiedot(self):
        print("Työntekijän tiedot:")
        print(f"Nimi: {self.nimi}")
        print(f"Ikä: {self.ika} vuotta")
        print(f"Palkka: {self.palkka} €")
        print(f"Osasto: {self.osasto}")
        print(f"Työkokemus: {self.tyoKokemus} vuotta")
    

