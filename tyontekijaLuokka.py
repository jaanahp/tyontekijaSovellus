class Tyontekija:
    nimi = ""
    tyoKokemus = 0
    palkka = 0.00

    def __init__ (self, n, p, k):
        self.nimi = n
        self.palkka = p
        self.tyoKokemus = k
    
    def tulostaTT(self):
        print(f"Työntekijä: {self.nimi}")
        print(f"Palkka €: {self.palkka}")
        print(f"Työkokemus vuosina: {self.tyoKokemus}")
    
    def nostaPalkkaa(self, n):
        self.palkka = self.palkka + n

class Harjoittelija(Tyontekija):
    kesto = 0

    def __init__(self, n, p, k, v):
        Tyontekija.__init__(self, n, p, k)
        self.kesto = v
    
    def tulostaH(self):
        print(f"Työntekijä: {self.nimi}")
        print(f"Palkka: {self.palkka}")
        print(f"Työkokemus: {self.tyoKokemus}")
        print(f"Harjoittelun kesto: {self.kesto} vuotta")



    

