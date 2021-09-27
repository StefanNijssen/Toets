Leeftijd = int(input("Wat is uw leeftijd?"))
Diploma = input("Heeft u een diploma in acteren?")
Geslacht = input("Bent u man of vrouw? M/V")
Lengte = int(input("Wat is uw lengte in centimeters?"))
Gewicht = int(input("Wat is uw gewicht?"))
Haar_kleur = input("Heeft u donker of blond haar?")


def leeftijd_diploma():
    if Leeftijd >= 18 and Diploma == 'ja':
        return True

def Man():
    Snor = input("Heeft u een Snor?")
    Kaal = input("Bent u kaal of bent u bereid kaal te gaan?")
    Bril = input("Heeft u een bril?")
    
    groenenwoud = Leeftijd >= 60 and Kaal == "ja" and Bril == "nee" and Snor == "nee"
    Van_Gelen = Leeftijd < 60 and Kaal == "nee" and Bril == "nee" or "ja" and Snor == "nee" and Haar_kleur == "donker"
    
    if Leeftijd >= 60:
        Groenenwoud()
    elif leeftijd < 60:


def Groenenwoud():
    groenenwoud = kaal == "ja" and Lengte <= 165 and Gewicht >= 90

if Geslacht == "M":
    Man()
else:
    Vrouw()