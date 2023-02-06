
munt1 = ["euro","dollar","yen","pond"]
munt2 = ["kroon","peso","roepi","lira","dollar"]
munt3 = ["zloty","euro","roepi","won","frank"]


def munt_toevoegen():
    munt = input("geef een munt.")
    box = input("in welke box gaat het 1,2,3")
    while(not munt == "stop"):
        if box == "1":
            munt1.append(munt)
            print("munt is in box 1")
            break
        elif box == "2":
            munt2.append(munt)
            print("munt is in box 2")
            break
        elif box == "3":
            munt3.append(munt)
            print("munt is in box 3")
            break
        else:
            print("ongelige antwoord ")
            munt = input("geef een munt.")
            box = input("in welke box gaat het 1,2,3")
def munten_lezen():
    keuze = input("welke lijst wilt u lezen")
    if keuze == "munt1":
        for munt in munt1[keuze]:
            print(munt)

def print_menu():
    print("1.voeg een munt toe")
    print("2.lees welke munt in het lijst zit")


#hoofdprogamma#

print_menu()
keuze = input("geef u keuze")
while (not keuze == "stop"):

    if keuze == "1":
        munt_toevoegen()
    elif keuze == "2":
        munten_lezen()

    else:
        print("ongeldige antwoord")
    print_menu()
    keuze = input("geef u keuze")


