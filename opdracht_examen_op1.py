from prettytable import PrettyTable


gidsen = {"gids1":{"naam":"Tom","leeftijd":25,"geslacht":"man","loon":2200,"steden":["genk",]},
          "gids2":{"naam":"Dario","leeftijd":23,"geslacht":"man","loon":2100,"steden":["hasselt",]},
          "gids3":{"naam":"Daisy","leeftijd":30,"geslacht":"vrouw","loon":1200,"steden":["maasmechelen",]},
          "gids4":{"naam":"Lennert","leeftijd":28,"geslacht":"man","loon":2700,"steden":["beringen",]},
          "gids5":{"naam":"Dries","leeftijd":40,"geslacht":"man","loon":2400,"steden":["bilzen",]}
          }

admin = {"admin1" : {
        "dario" : "inter",
         }}
def toon_Gidsen():
    P_table = PrettyTable(["ID","Naam", "leeftijd" ,"geslacht", "maandloon", "steden"])
    for id, persoon in gidsen.items():
        P_table.add_row([id,persoon["naam"],persoon["leeftijd"] ,persoon["geslacht"], persoon["loon"], persoon["steden"]])
    print(P_table)
def toon_menu():
    P_table = PrettyTable(["Nummer", "keuze"])
    P_table.add_row(["1.", "Voeg een Gids toe"])
    P_table.add_row(["2.", "voeg een stad toe aan een gids"])
    P_table.add_row(["3.", "verwijder een gids"])
    P_table.add_row(["4.", "voeg een stad toe aan alle gidsen"])
    P_table.add_row(["5.", "verander het wachtwoord van Admin"])
    P_table.add_row(["6.", "menu filters"])
    print(P_table)
def voeg_Gids_toe():
    id = input("geef de ID in van de gids ")
    naam = input("geef het naam van de niewue gids in")
    geslacht = input("is het een man/vrouw?")
    maandloon = int(input("geef aan hoeveel hij per maand verdient"))
    gidsen.update({id:{"naam":naam,"geslacht":geslacht,"jaar_indienst":0,"maandloon":maandloon}})
    print("nieuw personelslid is toegevoegd")
def voeg_een_stad_toe():
    toon_Gidsen()
    print("bij wie wil je een nieuwe stad toevoegen")
    naam = input("geef naam in van wie je de stad wil toevoegen")
    nieuwe_stad = input("geef een nieuwe stad in")
    for id,persoon in gidsen.items():
        if persoon["naam"] == naam:
            persoon["steden"].append(nieuwe_stad)
            toon_Gidsen()
def verwijder_een_gids():
    toon_Gidsen()
    persoon_id = input("welke persoon wilt u verwijderen geef aan met ID")
    del gidsen[persoon_id]
    toon_Gidsen()
def voeg_stad_toe_iedereen():
    nieuwe_stad = input("geef een nieuwe stad in")
    for id,persoon in gidsen.items():
        persoon["steden"].append(nieuwe_stad)
        toon_Gidsen()
def verander_wachtwoord():
    oud_wachtwoord = input("geef het oud wachtwoord in.")
    nieuw_wachtwoord = input("geef het nieuwe wachtwoord in .")
    nieuw_wachtwoord2 = input("geef het nieuwe wachtwoord in .")
    if nieuw_wachtwoord2 == nieuw_wachtwoord:
        print("correct")
        for man in admin.values():
            if man["dario"]== oud_wachtwoord:
                man["dario"]=nieuw_wachtwoord
                print(admin)
    else:
        print("ww  was fout probeer opnieuw")
def menu_filter():
    P_table = PrettyTable(["letter", "filter"])
    P_table.add_row(["a.", "alle man/vrouw gidsen"])
    P_table.add_row(["b.", "Alle gidsen die stad x gidsen"])
    P_table.add_row(["c.", "Alle gidsen met een hoger loon dan x"])
    P_table.add_row(["d.", "Alle man of vrouw die een stad gidse"])
    print(P_table)
def sort_geslacht():
    keuze = input("welk geslacht word er gekozen")
    P_table = PrettyTable(["Naam","geslacht","leeftijd","loon","steden"])
    for id,persoon in gidsen.items():
        if persoon["geslacht"] == keuze:
            P_table.add_row([persoon["naam"],persoon["geslacht"],persoon["leeftijd"],persoon["loon"],persoon["steden"]])
    print(P_table)
def toon_steden():
    keuze = input("geef aan welke gids u wilt zien met deze stad")
    P_table = PrettyTable(["Naam","geslacht","leeftijd","loon","steden"])
    for id,persoon in gidsen.items():
        if persoon["steden"] == [keuze]:
            P_table.add_row([persoon["naam"],persoon["geslacht"],persoon["leeftijd"],persoon["loon"],persoon["steden"]])
    print(P_table)
def vergelijken_van_maandloon():
    bedrag = int(input("geef het bedrag die hoger is die je wilt vergelijken"))
    P_table = PrettyTable(["Naam","geslacht","leeftijd","loon","steden"])
    for id,persoon in gidsen.items():
        if persoon["loon"] > bedrag:
            P_table.add_row([persoon["naam"],persoon["geslacht"],persoon["leeftijd"],persoon["loon"],persoon["steden"]])
    print(P_table)

#HoofdPrograma#


keuze = input("wil je stoppen?(type stop)")
while not (keuze == "stop"):
    toon_menu()
    keuze = input("kies uit het keuze tabel met het nummer")
    if keuze == "1":
        voeg_Gids_toe()
    elif keuze == "2":
        print("enkel admins mogen deze functie gebruiken log in.")
        ID = input("geef ID in.")
        username = input("geef u username in.")
        wachtwoord = input("geef het wachtwoord in.")
        while True:
            if wachtwoord in admin[ID][username]:
                print("welcome",username)
                voeg_een_stad_toe()
    elif keuze == "3":
        print("enkel admins mogen deze functie gebruiken log in.")
        ID = input("geef ID in.")
        username = input("geef u username in.")
        wachtwoord = input("geef het wachtwoord in.")
        while True:
             if wachtwoord in admin[ID][username]:
                print("welcome",username)
                verwijder_een_gids()
                break
    elif keuze == "4":
        voeg_stad_toe_iedereen()
    elif keuze == "5":
        verander_wachtwoord()
    elif keuze == "6":
        menu_filter()
        keuze = input("geef aan welke filter u wilt gebruien met letter")
        if keuze == "a":
            sort_geslacht()
        elif keuze == "b":
            toon_steden()
        elif keuze == "c":
            vergelijken_van_maandloon()
        elif keuze == "d":
            toon_steden()





