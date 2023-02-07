import string
from prettytable import PrettyTable




personeel = {
    "persoon1":{"naam":"dario","geslacht":"man","afdeling":"slagerij","jaar_indienst":1,"maandloon":1900},
    "persoon2":{"naam":"thomas","geslacht":"man","afdeling":"slagerij","jaar_indienst":12,"maandloon":1900},
    "persoon3":{"naam":"damiano","geslacht":"man","afdeling":"keuken","jaar_indienst":20,"maandloon":2500},
    "persoon4":{"naam":"marco","geslacht":"man","afdeling":"slagerij","jaar_indienst":40,"maandloon":5000},
    "persoon5":{"naam":"daisy","geslacht":"vrouw","afdeling":"bediening","jaar_indienst":5,"maandloon":1700},
    "persoon6":{"naam":"bianca","geslacht":"vrouw","afdeling":"slagerij","jaar_indienst":12,"maandloon":1850},
    "persoon7":{"naam":"rozzeta","geslacht":"man","afdeling":"bediening","jaar_indienst":20,"maandloon":2000},
    "persoon8":{"naam":"pino","geslacht":"man","afdeling":"keuken","jaar_indienst":5,"maandloon":2800},
    "persoon9":{"naam":"stefano","geslacht":"man","afdeling":"slagerij","jaar_indienst":4,"maandloon":1000},
    "persoon10":{"naam":"luca","geslacht":"man","afdeling":"slagerij","jaar_indienst":1,"maandloon":1000}
          }
admin = {"admin1" : {
        "dario" : "inter",
         }}
vergrendeld = "inter"
shift = 4
alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet,shifted)

encrypted = vergrendeld.translate(table)


def toon_admin():
    table = PrettyTable(["ID","username","wachtwoord","encrypted"])
    table.add_row(["admin1","dario","inter",encrypted])
    print(table)
def sort_geslacht():
    keuze = input("welk geslacht word er gekozen")
    P_table = PrettyTable(["Naam","geslacht","afdeling","jaar_indienst","maandloon"])
    for id,persoon in personeel.items():
        if persoon["geslacht"] == keuze:
            P_table.add_row([persoon["naam"],persoon["geslacht"],persoon["afdeling"],persoon["jaar_indienst"],persoon["maandloon"]])
    print(P_table)
def toon_afdeling():
    keuze = input("geef aan wie in welke afdeling werkt")
    P_table = PrettyTable(["Naam", "geslacht", "afdeling", "jaar_indienst", "maandloon"])
    for id,persoon in personeel.items():
        if persoon["afdeling"] == keuze:
            P_table.add_row([persoon["naam"],persoon["geslacht"],persoon["afdeling"],persoon["jaar_indienst"],persoon["maandloon"]])
    print(P_table)
def vergelijken_van_maandloon():
    bedrag = int(input("geef het bedrag die hoger is die je wilt vergelijken"))
    P_table = PrettyTable(["Naam", "geslacht", "afdeling", "jaar_indienst", "maandloon"])
    for id,persoon in personeel.items():
        if persoon["maandloon"] > bedrag:
            P_table.add_row([persoon["naam"],persoon["geslacht"],persoon["afdeling"],persoon["jaar_indienst"],persoon["maandloon"]])
    print(P_table)
def toon_wie_langer_dan_werkt():
    jaar = int(input("geef het jaar in waar je mee wilt vergelijken"))
    P_table = PrettyTable(["Naam", "geslacht", "afdeling", "jaar_indienst", "maandloon"])
    for id,persoon in personeel.items():
        if persoon["jaar_indienst"] > jaar:
            P_table.add_row([persoon["naam"],persoon["geslacht"],persoon["afdeling"],persoon["jaar_indienst"],persoon["maandloon"]])
    print(P_table)
def toon_persooneel():
    P_table = PrettyTable(["Naam", "geslacht", "afdeling", "jaar_indienst", "maandloon"])
    for id, persoon in personeel.items():
        P_table.add_row([persoon["naam"], persoon["geslacht"], persoon["afdeling"], persoon["jaar_indienst"], persoon["maandloon"]])
    print(P_table)
def toon_filter_menu():
    P_table = PrettyTable(["Nummer","lijst"])
    P_table.add_row(["1.","toon alle vrouw/man"])
    P_table.add_row(["2.","toon iedereen van een afdeling"])
    P_table.add_row(["3.","toon iedereen die meer verdient dan x per maand"])
    P_table.add_row(["4.","toon iedereen die langer dan x jaar in dienst is"])
    print(P_table)
def voeg_personeelslid_toe():
    id = input("geef de ID in ")
    naam = input("geef het naam van de niewue personeelslid in")
    geslacht = input("is het een man/vrouw?")
    afdeling = input("in welke afdeling werk de persoon")
    maandloon = int(input("geef aan hoeveel hij per maand verdient"))
    personeel.update({id:{"naam":naam,"geslacht":geslacht,"afdeling":afdeling,"jaar_indienst":0,"maandloon":maandloon}})
    print("nieuw personelslid is toegevoegd")
def voeg_personeelsleden_toe():
    keuze = input("wil je een personeelslid toevoegen")
    while not (keuze == "nee"):
        id = input("geef de ID in ")
        naam = input("geef het naam van de niewue personeelslid in")
        geslacht = input("is het een man/vrouw?")
        afdeling = input("in welke afdeling werk de persoon")
        maandloon = int(input("geef aan hoeveel hij per maand verdient"))
        personeel.update({id:{"naam":naam,"geslacht":geslacht,"afdeling":afdeling,"jaar_indienst":0,"maandloon":maandloon}})
        print("nieuw personelslid is toegevoegd")
        keuze = input("wil je een personeelslid toevoegen")
def verwijder_personeelslid():
    toon_persooneel()
    P_table = PrettyTable(["Naam", "geslacht", "afdeling", "jaar_indienst", "maandloon"])
    persoon_id = input("welke persoon wilt u verwijderen geef aan met ID")
    naam = input("geef het naam in die u wilt verwijderen")
    del personeel[persoon_id]
    toon_persooneel()
def verhoog_loon():
    toon_persooneel()
    persoonG = input("welke persoon wilt u het loon verhogen?")
    nieuw_loon = int(input("geef het nieuwe loon in"))
    P_table = PrettyTable(["Naam", "geslacht", "afdeling", "jaar_indienst", "maandloon"])
    for id,persoon in personeel.items():
        if persoon["naam"] == persoonG:
            persoon["maandloon"] = nieuw_loon
        P_table.add_row([persoon["naam"], persoon["geslacht"], persoon["afdeling"], persoon["jaar_indienst"],
                             persoon["maandloon"]])
    print(P_table)
def toon_menu():
    table = PrettyTable(["Nummer","Menu"])
    table.add_row(["1.","Toon admin menu"])
    table.add_row(["2.","voeg een personeelslid toe"])
    table.add_row(["3.","voeg personeelsleden toe"])
    table.add_row(["4.","verwijder een personeelslid"])
    table.add_row(["5.","verhoog loon van personeelslid"])
    table.add_row(["6","verhoog alle lonen"])
    table.add_row(["7.","toon admins"])
    print(table)
def verhoog_alle_loon():
    extra_loon = int(input("geef aan hoeveel u extra wilt geven per maand"))
    P_table = PrettyTable(["Naam", "geslacht", "afdeling", "jaar_indienst", "maandloon"])
    for id,persoon in personeel.items():
         persoon["maandloon"] += extra_loon
         P_table.add_row([persoon["naam"], persoon["geslacht"], persoon["afdeling"], persoon["jaar_indienst"],persoon["maandloon"]])
    print(P_table)
#hoofdprogama#
def log_in():
    id = input("geef aan welke admin id")
    naam = input("enter username")
    ask = input("enter pin")
    while True:
        if ask in admin[id][naam]:
            print("welcome",naam)
            toon_menu()
            keuze = input("geef aan wat u wilt doen met (kies uit lijst Nummer)")
            while not (keuze == "stop"):
                if keuze == "1":
                    toon_admin()
                elif keuze == "2":
                    voeg_personeelslid_toe()
                elif keuze == "3":
                    voeg_personeelsleden_toe()
                elif keuze == "4":
                    verwijder_personeelslid()
                elif keuze == "5":
                    verhoog_loon()
                elif keuze == "6":
                    verhoog_alle_loon()
                elif keuze == "7":
                    toon_admin()
                elif keuze == "8":
                    toon_filter_menu()
                    keuze = input("geef u keuze uit het lijst filter met het getal")
                    if keuze == "1":
                        sort_geslacht()
                    elif keuze == "2":
                        toon_afdeling()
                    elif keuze == "3":
                        vergelijken_van_maandloon()
                    elif keuze == "4":
                        toon_wie_langer_dan_werkt()
                toon_menu()
                keuze = input("geef aan wat u wilt doen met (kies uit lijst cijfer)")
        else:
            print("false name or pin.")
            id = input("geef aan welke id")
            naam = input("enter username")
            ask = input("enter pin")


log_in()