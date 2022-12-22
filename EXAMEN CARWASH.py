
prijs: list[float | int] =[]
wagen = []
verzekering = []
dagen1 = []
kmkosten: list[float | int] =[]
btw =1.21



print("welkom bij Cascus wagenverhuur uit welke "
      "categorie wilt u kiezen en kies aan met welke nummer voor auto?")
print('Categorie A : Ford Fiesta(1), Volkwagen polo(2)')
print('Categorie B: Ford Focus(3), Audi A3(4), Mercedes A klasse(5)')
print('Categorie C: Audi A4(6), Bmw 3(7), Mercedes C klasse 95(8)')
AUTO = input("-")

if AUTO == 1 or 2:
    print("categorie A kost 45 euro per dag ex btw")
    prijs.append(45)
    wagen.append(45)
elif AUTO == 3 or 4 or 5:
    print("categorie B kost 55 euro per dag ex btw")
    prijs.append(55)
    wagen.append(55)
elif AUTO == 6 or 7 or 8:
    print("categorie C kost 75 euro per dag ex btw")
    prijs.append(75)
    wagen.append(75)
else:
    print("kies AUB uit de categorie met een nummer.")


print("voor hoeveel dagen wilt u de auto huren?")
dagen = int(input())
dagen1.append(dagen)

print("uit welke verzekering wilt u kiezen?"
      "A = standaard of B = full omnium?")

verzekering = input("-")

if verzekering.upper() == 'A':
    print("u kiest voor standaard dat kost 20% van u huurprijs + 20 ex btw")
    prijs.append(1.20+20)

elif verzekering.upper()  == 'B':
    print("u kiest full omnium dat kost u 30% van de huur prijs + 25 euro ex btw")

    prijs.append(1.30+25)
else:
    print("kies uit A of B aub")

print("hoeveel KM heeft u gereden met de auto?")
print("dit is 12 cent vanaf meer dan 100 km ")

km = float(input("-"))

if km > 100:
    print("u heeft meer dan 100 km gereden dat kost u meer")
    print("hoeveel km heb je extra gereden boven 100?")
    kmExtra = float(input("-"))

    kmkosten.append(kmExtra*0.12)

else:
    print("u zit onder 100km")






print("dit is de berekening/factuur")
print("kosten van wagen",wagen)
print("aantal dagen",dagen)
print("aantal km",km)
print("prijs aantal km",kmkosten)
print("prijs zonder btw",(sum(prijs)))


print("btw",btw)
print("prijs inc btw",(sum(prijs)*btw))



