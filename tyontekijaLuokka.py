#--- Pääluokka --- 
class Tyontekija:
    nimi = ""
    tyoKokemus = 0
    palkka = 0.00

    def __init__ (self, n, p, k):
        self.nimi = n
        self.palkka = p
        self.tyoKokemus = k
    
    def palkkaVertailu(self):
        minimipalkka = 2300.00
        print(f"Nimi: {self.nimi}")
        print(f"Palkka: {self.palkka} €")
        print(f"Työkokemus: {self.tyoKokemus} vuotta")
        if self.palkka < minimipalkka and self.tyoKokemus >= 5:
            print(f"Palkka alle minimin, nosta palkkaa {minimipalkka - self.palkka} € ")
        elif self.palkka < minimipalkka and self.tyoKokemus < 5:
            palkankorotus = (minimipalkka - self.palkka) * 0.75
            print(f"Palkka alle minimin {minimipalkka} €, nosta palkkaa {palkankorotus} €")
        else:
            print(f"Palkka {self.palkka} €, minimipalkka {minimipalkka} €, ei korotustarvetta")
    
    def tulostaTT(self):
        print(f"Työntekijä: {self.nimi}")
        print(f"Palkka €: {self.palkka}")
        print(f"Työkokemus vuosina: {self.tyoKokemus}")
    
    def nostaPalkkaa(self, n):
        self.palkka = self.palkka + n

#--- Alaluokka --- 
class Harjoittelija(Tyontekija):
    kesto = 0

    def __init__(self, n, p, k, v):
        Tyontekija.__init__(self, n, p, k)
        self.kesto = v

    def harjoittelunKesto(self):
        harjoittelu = 3
        print(f"Nimi: {self.nimi}")
        print(f"Muu työkokemus vuosina: {self.tyoKokemus}")
        print(f"Harjoittelua vuosina: {self.kesto}")
        if self.kesto >= harjoittelu:
            print(f"Harjoittelu {harjoittelu} vuotta ohi, siirrä harjoittelija työntekijäksi")
        elif self.kesto < harjoittelu and self.tyoKokemus >= 5:
            print(f"Harjoittelua {harjoittelu} vuotta kuitattu työkokemuksella, siirrä harjoittelija työntekijäksi")
        else:
            print(f"Harjoittelu jatkuu vielä {harjoittelu - self.kesto} vuotta")
    
    def tulostaH(self):
        print(f"Työntekijä: {self.nimi}")
        print(f"Palkka: {self.palkka}")
        print(f"Työkokemus: {self.tyoKokemus}")
        print(f"Harjoittelun kesto: {self.kesto} vuotta")



    

