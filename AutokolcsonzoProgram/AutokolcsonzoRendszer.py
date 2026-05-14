
from abc import ABC
from datetime import datetime
import os


class Auto(ABC):
    def __init__(self, rendszam, tipus, berletiDij):
        self._rendszam = rendszam
        self._tipus = tipus
        self._berletiDij = berletiDij


class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berletiDij, ulesek_szama):
        super().__init__(rendszam, tipus, berletiDij)
        self._ulesek_szama = ulesek_szama


class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berletiDij, teherbiras):
        super().__init__(rendszam, tipus, berletiDij)
        self._teherbiras = teherbiras


class Autokolcsonzo:
    def __init__(self, nev):
        self._nev = nev
        self._autok = []
        self._berlesek = []


class Berles:
    def __init__(self, auto, datum):
        self._auto = auto
        self._datum = datum


def Elokeszites():
    # Kölcsönzõ létrehozása
    kolcsonzo = Autokolcsonzo("AutoKocsonzo")

    # Autók létrehozása
    auto1 = Szemelyauto("ABC-123", "Toyota Corolla", 10000, 5)
    auto2 = Szemelyauto("DEF-456", "Honda Civic", 12000, 5)
    auto3 = Teherauto("GHI-789", "Ford Transit", 20000, 1500)

    # Autók hozzáadása
    kolcsonzo._autok.append(auto1)
    kolcsonzo._autok.append(auto2)
    kolcsonzo._autok.append(auto3)

    # Bérlések létrehozása
    berles1 = Berles(auto1, "2026-05-10")
    berles2 = Berles(auto2, "2026-05-11")
    berles3 = Berles(auto3, "2026-05-12")
    berles4 = Berles(auto1, "2026-05-13")

    # Bérlések hozzáadása
    kolcsonzo._berlesek.append(berles1)
    kolcsonzo._berlesek.append(berles2)
    kolcsonzo._berlesek.append(berles3)
    kolcsonzo._berlesek.append(berles4)

    return kolcsonzo


def AutoBerles():
    print("\n\n--Auto Berles--\n")
    sorszam = 0
    for auto in kolcsonzo._autok:
        sorszam += 1
        print(str(sorszam) + " - " + auto._tipus)

    try:
        ValasztottAuto = int(input("\nBerelni kivant auto sorszama: ")) - 1
        if -1 < ValasztottAuto < len(kolcsonzo._autok):
            valasztottDatum = datetime.strptime(input("Adja meg a berles datumat: (eeee-hh-nn): "), "%Y-%m-%d").date()
            if valasztottDatum < datetime.now().date():
                print("A valasztott datum hibas!")
                return Menu()
            valasztottDatum = str(valasztottDatum)

            UjBerles = Berles(kolcsonzo._autok[int(ValasztottAuto)], valasztottDatum)
            for berles in kolcsonzo._berlesek:
                if berles._auto == kolcsonzo._autok[ValasztottAuto] and berles._datum == valasztottDatum:
                    print("Erre a napra ez a jarmu mar le lett foglalva!")
                    return Menu()
        else:
            print("Ilyen sorszamu auto nem talalhato a rendszerben")
            return Menu()
    except:
        print("Hibasan megadott adat!")
        return Menu()

    kolcsonzo._berlesek.append(UjBerles)

    Auto = kolcsonzo._autok[int(ValasztottAuto)]
    print("Uj berles feljegyezve. Fizetendo osszeg: " + str(Auto._berletiDij))
    return Menu()

def BerlesekLista():
    print("\n\n--Berlesek Listaja--\n")
    for berles in kolcsonzo._berlesek:
        print(str(berles._auto._tipus) + ", " + str(berles._datum))
    return Menu()

def BerlesLemondas():
    print("\n\n--Berles Lemondas--\n")
    sorszam = 0
    print("Berlesek:")
    for berles in kolcsonzo._berlesek:
        sorszam += 1
        print(str(sorszam) + " - " + str(berles._auto._tipus) + ", " + str(berles._datum))

    try:
        valasztottAuto = int(input("\nTorolni kivant berles sorszama: ")) - 1
        kolcsonzo._berlesek.pop(valasztottAuto)
    except:
        print("Hibas adat!")
        return Menu()

    return Menu()

def Menu():
    print("\n\n--Autokolcsonzo Alkalmazas--\n")
    print("1 - Auto Berles")
    print("2 - Berlesek Listaja")
    print("3 - Berles Lemondasa")
    print("4 - Kilepes")

    try:
        valasztottFunkcio = int(input("\nA hasznalni kivant Funkcio sorszama: "))
    except:
        print("Hibas adat!")
        return Menu()

    if valasztottFunkcio == 1:
        return AutoBerles()
    elif valasztottFunkcio == 2:
        return BerlesekLista()
    elif valasztottFunkcio == 3:
        return BerlesLemondas()
    elif valasztottFunkcio == 4:
        print("Kilepes...")
    else:
        print("!!! Adja meg az egyik Funkcio sorszamat !!!")
        return Menu()


kolcsonzo = Elokeszites()
Menu()


