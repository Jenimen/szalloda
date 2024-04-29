from datetime import datetime

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 5000)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 8000)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class FoglalasKezelo:
    def __init__(self, szalloda):
        self.szalloda = szalloda
        self.foglalasok = []

    def foglalas(self, szobaszam, datum):
        for szoba in self.szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas_datum = datetime.strptime(datum, "%Y-%m-%d")
                today = datetime.today()
                if foglalas_datum < today:
                    return "A foglalás csak jövőbeli dátumra lehetséges."
                for foglalas in self.foglalasok:
                    if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                        return "A szoba már foglalt ezen a napon."
                self.foglalasok.append(Foglalas(szoba, datum))
                return f"A {szobaszam} szobára sikeresen foglaltak {datum}-ra."
        return "A megadott szobaszám nem létezik a szállodában."

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return f"A {szobaszam} szoba foglalása {datum}-ra sikeresen törölve."
        return "A megadott foglalás nem található."

    def listaz_foglalasok(self):
        if not self.foglalasok:
            return "Nincsenek foglalások."
        foglalasok_str = "Foglalások:\n"
        for foglalas in self.foglalasok:
            foglalasok_str += f"Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}\n"
        return foglalasok_str

# Szálloda, szobák és foglalások inicializálása
szalloda = Szalloda("Pihenés Hotel")
szalloda.add_szoba(EgyagyasSzoba("101"))
szalloda.add_szoba(EgyagyasSzoba("102"))
szalloda.add_szoba(KetagyasSzoba("201"))
szalloda.add_szoba(KetagyasSzoba("202"))
szalloda.add_szoba(KetagyasSzoba("203"))

foglalas_kezelo = FoglalasKezelo(szalloda)
foglalas_kezelo.foglalas("101", "2024-04-25")
foglalas_kezelo.foglalas("201", "2024-04-27")
foglalas_kezelo.foglalas("202", "2024-04-30")
foglalas_kezelo.foglalas("102", "2024-05-01")
foglalas_kezelo.foglalas("203", "2024-05-02")

# Felhasználói interfész
def menu():
    print("\nVálasszon műveletet:")
    print("1. Foglalás")
    print("2. Lemondás")
    print("3. Foglalások listázása")
    print("0. Kilépés")

def main():
    while True:
        menu()
        valasztas = input("Kérem válasszon: ")
        if valasztas == "1":
            szobaszam = input("Adja meg a szobaszámot: ")
            datum = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN): ")
            print(foglalas_kezelo.foglalas(szobaszam, datum))
        elif valasztas == "2":
            szobaszam = input("Adja meg a szobaszámot: ")
            datum = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN): ")
            print(foglalas_kezelo.lemondas(szobaszam, datum))
        elif valasztas == "3":
            print(foglalas_kezelo.listaz_foglalasok())
        elif valasztas == "0":
            print("Kilépés...")
            break
        else:
            print("Nem megfelelő választás, kérem válasszon újra.")

if __name__ == "__main__":
    main()

