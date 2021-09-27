Leeftijd = int(input("Wat is uw leeftijd?"))
Diploma = input("Heeft u een diploma in acteren?")
Geslacht = input("Bent u man of vrouw? M/V")
Lengte = int(input("Wat is uw lengte in centimeters?"))
Gewicht = int(input("Wat is uw gewicht?"))

def leeftijd_diploma():
    if Leeftijd >= 18 and Diploma == 'ja':
        return True

def Man():
    if Leeftijd >= 60:
        in

def Groenenwoud():
    kaal = input("Bent u kaal of bent u bereid om kaal te gaan?")
    if kaal == "ja":
        if Lengte <= 165:
            if Gewicht >= 90:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    