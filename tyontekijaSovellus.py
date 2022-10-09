from tyontekijaLuokka import Tyontekija
from tyontekijaLuokka import Harjoittelija

#--- Funktiot ---

def tietojenSyotto():
    syotaTiedot = "T"
    while syotaTiedot != "L":
        syotaTiedot = input("Valitse T syöttääksesi uuden työntekijän tiedot, H syöttääksesi harjoittelijan tiedot ja L lopettaaksesi: ").upper()
        if syotaTiedot == "T":
            nimi = input("Anna työntekijän nimi: ")
            palkka = float(input("Anna työntekijän palkka: "))
            kokemus = int(input("Anna työntekijän kokemus vuosina: "))
            uusiTT = Tyontekija(nimi, palkka, kokemus)
            tyontekijaLista.append(uusiTT)
        elif syotaTiedot == "H":
            nimi = input("Anna työntekijän nimi: ")
            palkka = float(input("Anna harjoittelijan palkka: "))
            kokemus = int(input("Anna harjoittelijan kokemus vuosina: "))
            kesto = int(input("Anna harjoitteluaika vuosina: "))
            uusiH = Harjoittelija(nimi, palkka, kokemus, kesto)
            harjoittelijaLista.append(uusiH)
        elif syotaTiedot == "L":
            break

def osioMerkki():
    print("------------------------------------------------------------------------------------")

def tulostaPalkat():
    osioMerkki()
    print("Palkkavertailu:")
    for tt in tyontekijaLista:
        tt.palkkaVertailu(minimi)

def tulostaHarjoittelut():
    osioMerkki()
    print("Harjoittelujen kesto:")
    for h in harjoittelijaLista:
        h.harjoittelunKesto(harjoittelu)

def muutaPalkkaa():
    palkanMuutos = "K"
    osioMerkki()
    while palkanMuutos != "E":
        palkanMuutos = input("Haluatko muuttaa työntekijän palkkaa? K = Kyllä, E = Ei: ").upper()
        if palkanMuutos == "K":
            y = 1
            for t in tyontekijaLista:
                print(f"Numero {y}:{t.nimi}")
                y+= 1
            numero = int(input("Valitse työntekijän numero: "))
            index = numero - 1
            korotus = int(input("Anna korotuksen määrä euroina: "))
            tyontekijaLista[index].nostaPalkkaa(korotus)
        elif palkanMuutos == "E":
            break

#--- Pääohjelma --- 
print("Palkkavertailu")
minimi = float(input("Anna minimipalkka: "))
harjoittelu = int(input("Anna harjoittelun maksimikesto vuosina: "))
tyontekijaLista = []
harjoittelijaLista = []

tietojenSyotto()

print("Tietojen syöttö valmis")
tulostaPalkat()
tulostaHarjoittelut()
    
osioMerkki()
muutaPalkkaa()

print("Ohjelma päättyi")

for t in tyontekijaLista:
    t.tulostaTT()

