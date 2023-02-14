from prettytable import PrettyTable

list_woorden = ["dario","maasmechelen","python"]
dict = {"key":list_woorden[0],"valeu":list_woorden[1]}


def functie_lijst_dict():
    b = dict(zip(list_woorden[::1],list_woorden[0::2]))
    print(b)

def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result
def voeg_toe_aan_lijst():
    woord = input("geef aan wat u wilt toevoegen")
    list_woorden.append(woord)
    print("gelukt")

def verwijder_woord():
    print(list_woorden)
    woord = input("geef aan wat u wilt verwijderen ")
    list_woorden.remove(woord)
def toon_menu():
    P_table = PrettyTable(["Nummer", "keuze"])
    P_table.add_row(["1.", "Voeg woord toe aan lijst"])
    P_table.add_row(["2.", "verwijder woord uit lijst"])
    P_table.add_row(["3.", "toon lijst"])
    P_table.add_row(["4.", "encrypt tekst"])
    print(P_table)


#hoofdprograma


keuze = input("wil je stoppen?(type stop)")
while not (keuze == "stop"):
    toon_menu()
    keuze = input("geef aan wat u wilt doen nummer")
    if keuze == "1":
        voeg_toe_aan_lijst()
    elif keuze == "2":
        verwijder_woord()
    elif keuze == "3":
        print(list_woorden)
    elif keuze == "4":
        getal = int(input("hoeveel keer moet het verspringen"))
        encrypt(list_woorden,4)