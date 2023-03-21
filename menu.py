from prettytable import PrettyTable

class Werknemer:

    def __init__(self,id,naam,geslacht):
        self.id = id
        self.naam = naam
        self.geslacht = geslacht

class Bediende(Werknemer):

    def __init__(self,id,naam,geslacht,maandloon):
        super().__init__(id.id, naam, geslacht)
        self.maandloon = maandloon

    def toon_info_bediende(self):
        print("deze bediende met naam {} is een {} en verdient per maand {}".format(self.naam,self.geslacht,self.maandloon))

class Arbeider(Werknemer):

    def __init__(self,id,naam,geslacht,uurloon):
        super().__init__(id, naam, geslacht)
        self.uurloon = uurloon

    def toon_info_arbeider(self):
        print("deze arbeider met de naam {} is een {} en verdient per maand {}".format(self.naam,self.geslacht,self.uurloon))





WA = Werknemer(1,"dario","man")
WA1 = Werknemer(2,"anna","vrouw")
WA2 = Werknemer(3,"angelo","man")
WA3 = Arbeider(4,"luca","man",14)

WA3.toon_info_arbeider()

arbeiders = [WA,WA1,WA2,WA3]

