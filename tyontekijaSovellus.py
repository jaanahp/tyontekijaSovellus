from tyontekijaLuokka import Tyontekija
from tyontekijaLuokka import Harjoittelija

print("Palkkavertailu")
tyontekijaLista = []
harjoittelijaLista = []
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

print("Tietojen syöttö valmis")
print("------------------------------------------------------------------------------------")
print("Palkkatiedot:")
for tt in tyontekijaLista:
    tt.palkkaVertailu()
print("------------------------------------------------------------------------------------")
print("Harjoittelujen kesto:")
for h in harjoittelijaLista:
    h.harjoittelunKesto()


