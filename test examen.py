print("welk geslacht hebt u?")
geslacht =input("-")


if geslacht.upper() == 'MAN':
    print("u ben  een man hoeveel km heeft u gefietst?")
    KMfiets = int(input())

    print("hoeveel km heeft u gelopen?")
    KMlopen= int(input())

    print("hoeveel km heeft u gezwomen?")
    KMzwem = int(input())

    if KMfiets > 20 and KMlopen >10 and KMzwem > 3:
        print("u bent geslaagt proficiat !")
    elif KMfiets > 50 and KMlopen >5 and KMzwem > 2:
        print("u bent geslaagt proficiat !")
    elif KMfiets > 45 and KMlopen >7 and KMzwem > 2:
        print("u bent geslaagt proficiat !")
    else:
        print('u bent helaas niet geslaagt')


if geslacht.upper() == 'VROUW':
    print("u ben  een man hoeveel km heeft u gefietst?")
    KMfiets = int(input())

    print("hoeveel km heeft u gelopen?")
    KMlopen= int(input())

    print("hoeveel km heeft u gezwomen?")
    KMzwem = int(input())

    if KMfiets > 15 and KMlopen >8 and KMzwem > 3:
        print("u bent geslaagt proficiat !")
    elif KMfiets > 25 and KMlopen >10 and KMzwem > 2:
        print("u bent geslaagt proficiat !")
    elif KMfiets > 40 and KMlopen >8 and KMzwem > 2:
        print("u bent geslaagt proficiat !")
    else:
        print('u bent helaas niet geslaagt')

