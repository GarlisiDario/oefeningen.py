A = []
D = []
H = []
V = []
def print_lijst():
    print("1.toon_lijst")
    print("2.voeg_naam_toe")
    print("3.zoek_in_lijst")
    print("4.verwijder_uit_lijst")
    print("5.sorteer_lijst")
def toon_lijst():
    keuze = input("kies welke lijst u wilt zien A,D,H,V")
    while not (keuze == "stop"):
      if keuze.upper() == 'A':
        print(A)
      elif keuze.upper() == 'D':
        print(D)
      elif keuze.upper() == 'H':
        print(H)
      elif keuze.upper() == 'V':
        print(V)
      else:
        print("geen geldig antwoord kies uit A,D,H,V")
      keuze = input("kies welke lijst u wilt zien A,D,H,V")
def voeg_naam_toe():
    naam = input("welke naam wilt u in geven")
    groep_lijst = input("in welke lijst mag het naam zich bevinden A,D,H,V")
    while not (naam == "stop"):
      if groep_lijst.upper() == "A":
        A.append(naam)
        print(f"{naam}-->zit nu in groep A")
      elif groep_lijst.upper() == "D":
        D.append(naam)
        print(f"{naam}-->zit nu in groep D")
      elif groep_lijst.upper()=="H":
        H.append(naam)
        print(f"{naam}-->zit nu in groep H")
      elif groep_lijst.upper()== "V":
        V.append(naam)
        print(f"{naam}-->zit nu in groep V")
      else:
        print("kies uit een van de geldige groepen")
      naam = input("welke naam wilt u in geven")
      groep_lijst = input("in welke lijst mag het naam zich bevinden A,D,H,V")
def zoek_in_lijst():
    naam = input("geef welke naam u wilt zoeken")
    if naam in A :
        print(f"{naam} zit in groep A")
    elif naam in D:
        print(f"{naam} izt in groep D")
    elif naam in H:
        print(f"{naam} zit in groep H")
    elif naam in V:
        print(f"{naam} zit in  groep V")
    else:
        print(f"{naam} zit niet in een groep")
def verwijder_uit_lijst():
    naam = input("geef welke naam u wilt zoeken")
    if naam in A:
        print(f"{naam} verwijderd uit groep A")
        A.remove(naam)
    elif naam in D:
        print(f"{naam} verwijderd uit groep D")
        D.remove(naam)
    elif naam in H:
        print(f"{naam} verwijderd uit groep H")
        H.remove(naam)
    elif naam in V:
        print(f"{naam} verwijderd uit  groep V")
        V.remove(naam)
    else:
        print(f"{naam} zit niet in een groep")
def sorteer_lijst():
    keuze = input("geef in wat u wilt sorteren")
    if keuze.upper() == "A":
        A.sort(reverse=True)
        print(A)
    elif keuze.upper() == "D":
        D.sort(reverse=True)
        print(D)
    elif keuze.upper() == "H":
        H.sort(reverse=True)
        print(H)
    elif keuze.upper() == "V":
        V.sort(reverse=True)
        print(V)
    else:
        print("error fout antwoord je bent dood")








#####################################################
#HOOFDPROGAMMA                                      #
#####################################################

print_lijst()
antwoord = input("kies uit lijst wat u wilt met nummer")
while not (antwoord == "stop"):
    if antwoord == "1":
        print(toon_lijst())
    elif antwoord == "2":
        print(voeg_naam_toe())
    elif antwoord == "3":
        print(zoek_in_lijst())
    elif antwoord == "4":
        print(verwijder_uit_lijst())
    elif antwoord == "5":
        print(sorteer_lijst())

    print_lijst()
    antwoord = input("kies uit lijst wat u wilt met nummer")



