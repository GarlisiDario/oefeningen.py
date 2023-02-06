cursesen = {"curses1":{"cursesnaam":"python","aantaluren":3}
            }



def toon_curses():
    print("---------------------------------------")
    print("ID","\t\t","cursesNaam","\t\t","uren")
    print("---------------------------------------")
    for id, curses in cursesen.items():
        print(id, end="\t\t")
        for info in curses.values():
            print(info, end="\t\t\t\t")
        print(" ")
    print("--------------------------------------------")
toon_curses()
def voeg_curses_toe():
    keuze = input("will je nog een curses toevoegen?")
    while(not keuze == "nee"):
        ID = input("geef u curses in ")
        curses_naam = input("geef het naam van de curses")
        aantal_uren = int(input("geef het aantal uren in hoelang het duurt"))
        cursesen.update({ID:{"cursesnaam":curses_naam,"aantaluren":aantal_uren}})
        keuze = input("will je nog een curses toevoegen?")
def wijzig_aantal_uren():
    curses_wijzigen = input("welke curses wilt u de uren wijzigen?")
    if curses_wijzigen in cursesen:
        nieuwe_uren = int(input("geef aan hoelang de curses zal duren"))
        cursesen[curses_wijzigen]["aantaluren"] = nieuwe_uren



voeg_curses_toe()
wijzig_aantal_uren()
toon_curses()


