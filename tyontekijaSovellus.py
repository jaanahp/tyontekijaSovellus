from tyontekijaLuokka import Tyontekija
from tyontekijaLuokka import Harjoittelija
import re

#--- Funktiot --- 
def ilmoitus():
    print("Tarkista syöttämäsi tieto")

def osioMerkki():
    print("------------------------------------------------------------------------------------")

#Funktiot työntekijän ja harjoittelijan ominaisuuksien luomiseen
def annaNimi():
    nimi = ""
    testi = False
    while testi != True:
        nimi = input("Anna koko nimi: ")
        #RegEx -testi tarkistaa, että nimi-muuttujaan syötetty tieto sisältää vain isoja tai pieniä kirjaimia väliltä a-ö [a-öA-Ö] tai tyhjää väliä (\s), samaa kirjainta saa olla useampikin (+) ja
        #sana voi myös päättyä näihin ($). Jos tämä pitää paikkansa, regex palauttaa testin tulokseksi True.
        testi = bool(re.match('[a-öA-Ö\s]+$', nimi))
    return nimi

def syotaPalkka():
    palkka = 0.00
    while palkka == 0.00:
        try:
            palkka = float(input("Anna palkka euroina: "))
        except:
            ilmoitus()
    return palkka

def syotaKokemus():
    kokemus = 0
    while kokemus == 0:
        try:
            kokemus = int(input("Anna työkokemus vuosina: "))
        except:
            ilmoitus()
    return kokemus

def syotaKesto():
    kesto = 0
    while kesto == 0:
        try: 
            kesto = int(input("Anna harjoittelun kesto vuosina tähän saakka: "))
        except:
            ilmoitus()
    return kesto

def syotaKorotus():
    korotus = 0.00
    while korotus == 0.00:
        try:
            korotus = float(input("Anna palkankorotus euroina: "))
        except:
            ilmoitus()
    return korotus

#Funktio työntekijöiden/harjoittelijoiden syöttämiseksi tyontekijaLista ja harjoittelijaLista -listoille
def tietojenSyotto():
    syotaTiedot = "T"
    while syotaTiedot != "L":
        syotaTiedot = input("Valitse T syöttääksesi uuden työntekijän tiedot, H syöttääksesi harjoittelijan tiedot ja L lopettaaksesi: ").upper()
        if syotaTiedot == "T":
            uusiTT = Tyontekija(annaNimi(), syotaPalkka(), syotaKokemus())
            tyontekijaLista.append(uusiTT)
        elif syotaTiedot == "H":
            uusiH = Harjoittelija(annaNimi(), syotaPalkka(), syotaKokemus(), syotaKesto())
            harjoittelijaLista.append(uusiH)
        elif syotaTiedot == "L":
            break

#Funktio työntekijän palkan muuttamiseksi
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
            if numero > len(tyontekijaLista) or numero < 1:
                ilmoitus()
            else:
                index = numero - 1
                tyontekijaLista[index].nostaPalkkaa(syotaKorotus())
        elif palkanMuutos == "E":
            break

#Funktio harjoittelijan siirtämiseksi työntekijäksi
def siirraHarj():
    siirto = "K"
    osioMerkki()
    while siirto != "E":
        siirto = input("Haluatko siirtää harjoittelijoita työntekijäluokkaan? K = Kyllä, E = Ei: ").upper()
        if siirto == "K":
            i = 1
            for h in harjoittelijaLista:
                print(f"Numero {i}:{h.nimi}")
                i+= 1
            numero = int(input("Valitse siirrettävän harjoittelijan numero: "))
            if numero > len(harjoittelijaLista) or numero < 1:
                ilmoitus()
            else:
                index = numero - 1
                tyontekijaLista.append(harjoittelijaLista[index])
                del harjoittelijaLista[index]    
        elif siirto == "E":
            break

#Funktiot palkka-/harjoittelutietojen vertailuun ja tulostamiseen
def tulostaPalkat():
    osioMerkki()
    print("Palkkavertailu:")
    for tt in tyontekijaLista:
        tt.palkkaVertailu(minimiPalkka)

def tulostaHarjoittelut():
    osioMerkki()
    print("Harjoittelujen kesto:")
    for h in harjoittelijaLista:
        h.harjoittelunKesto(harjoitteluKesto)

def tulostaTTlista():
    osioMerkki()
    print("Tulostetaan kaikki työntekijät:")
    for tt in tyontekijaLista: 
        tt.tulostaTT()

def tulostaHlista():
    osioMerkki()
    print("Tulostetaan kaikki harjoittelijat")
    for h in harjoittelijaLista:
        h.tulostaH()

#--- Pääohjelma --- 
print("Palkkojen ja harjoitteluaikojen vertailu")

#Luokkien vaatimat pohjatiedot ja niiden oikeellisuustarkistus
minimiPalkka = 0
harjoitteluKesto = 0
while minimiPalkka == 0:
    try:
        minimiPalkka = float(input("Syötä minimipalkka: "))
    except:
        ilmoitus()
while harjoitteluKesto == 0:
    try:
        harjoitteluKesto = int(input("Syötä harjoittelun maksimiaika vuosina: "))
    except:
        ilmoitus()

#Olioiden listat        
tyontekijaLista = []
harjoittelijaLista = []

vastaus = "K"

#Pääsilmukka
while vastaus != "E":
    tietojenSyotto()

    print("Tietojen syöttö valmis")
    tulostaPalkat()
    tulostaHarjoittelut()

    muutaPalkkaa()
    siirraHarj()

    print("Ohjelma valmis")
    tulostaTTlista()
    tulostaHlista()

    osioMerkki()
    vastaus = input("Haluatko jatkaa vertailua ja syöttää lisää työntekijöitä/harjoittelijoita? K = Kyllä, E = Ei: ").upper()

print("Ohjelma päättyi")

