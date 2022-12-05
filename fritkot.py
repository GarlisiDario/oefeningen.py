

K = (int(input("geef aan met hoeveel personen jullie zijn")))
F = ["kleine friet","middel friet","grote friet"]
EX = ["speciaal","stoofvleessaus"]
BTW = 1.21
saus3 = ["-A-op de frieten 0.5$","-B-klein bakje 0.5$","-C-grote bakje 0.80$"]
print("kies uit een van deze keuze vul in met a b c ",F)
aantal_keuze = [0,0,0]
prijs: list[float | int] =[]
aantal= 0
while aantal < K:
    keuze = input("/")
    if keuze.lower() == "a":
        aantal_keuze[0] += 1
        prijs.append(2.20)
        aantal += 1

    elif keuze.lower() == "b":
        aantal_keuze[1] += 1
        prijs.append(2.50)
        aantal += 1

    elif keuze.lower() == "c":
        aantal_keuze[2] += 1
        prijs.append(3.00)
        aantal += 1
    else:
        print("zit niet in het menu")


aantal = 0
while aantal < K:
 print("wilt u saus ja of nee")
 saus = str(input("-"))

 if saus.lower() == 'ja':
    print("welke saus wilt u kies uit  A-speciaal of B-stoofvleessaus")

    saus_keuze = str(input(""))

    if saus_keuze.lower() == "a":
        print("speciaal kost 1$ extra")
        prijs.append(1)

    elif saus_keuze.lower() == "b":
        print("stoofvleessaus kost u 1.8$ extra")
        prijs.append(1.8)
    else:
     print("fout melding kies uit A of B",EX)
 aantal += 1

aantal = 0
while aantal < K:
 print("wilt u er saus bij? ja of nee")
 saus2 = str(input("-"))

 if saus2.lower() == "ja":
  print("kies uit",saus3)
  saus_3 = str(input("-"))

  if saus_3.upper() == "A":
            print("boven de frieten kost 0.5$ extra")
            prijs.append(0.5)
  elif saus_3.upper() == "B":
            print("saus in klein potje kost u 0.5$ extra")
            prijs.append(0.5)
  elif saus_3.upper() == "C":
            print("saus in een groot bakje kost u 0.8$ extra")
            prijs.append(0.8)
  else:
            print("fout ingave kiest uit-->",saus3)
 aantal +=1

aantal=0
while aantal <K:
    print("wilt u er een frituursnack bij ? kies uit ja of nee.")
    snack = str(input("-"))
    if snack.lower() == "ja":
        print("welke snack zow u willen? A-Hamburger(frikandel)B-boulet C-Mexicano D-servola "
              "E-kipnuggets F-fingers G-Bicky burger ")
        snack_keuze = str(input("-"))
        if snack_keuze.lower() == "a":
            prijs.append(2.30)
        elif snack_keuze.lower()=="b":
            prijs.append(2.30)
        elif snack_keuze.lower()=="c":
            prijs.append(2.30)
        elif snack_keuze.lower() =="d":
            prijs.append(2.30)
        elif snack_keuze.lower()== "e":
            prijs.append(2.50)
        elif snack_keuze.lower()=="f":
            prijs.append(2.50)
        elif snack_keuze.lower() == "g":
            prijs.append(3.20)
    aantal +=1




print("prijs zonder BTW",prijs,sum(prijs))
print("BTW =21%")
print(sum(prijs)*BTW)

