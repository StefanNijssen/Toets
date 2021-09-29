Leeftijd = int(input("Wat is uw leeftijd?\n"))
Diploma = input("Heeft u een diploma in acteren?\n")
Geslacht = input("Bent u man of vrouw? M/V\n")
Lengte = int(input("Wat is uw lengte in centimeters?\n"))
Gewicht = int(input("Wat is uw gewicht?\n"))
Haar_kleur = input("Heeft u donker of blond haar?\n")


leeftijd_diploma = Leeftijd >= 18 and Diploma == 'ja':

def Man():
    Snor = input("Heeft u een Snor?\n")
    Kaal = input("Bent u kaal of bent u bereid kaal te gaan?\n")
    Bril = input("Heeft u een bril?\n")
    groenenwoud = leeftijd_diploma == True and Leeftijd >= 60 and Kaal == "ja" and Bril == "nee" and Snor == "nee" and Lengte <= 165 and Gewicht >= 90
    Van_Geelen = leeftijd_diploma == True and Leeftijd < 60 and Kaal == "nee" and Bril == "nee" or "ja" and Snor == "nee" and Haar_kleur == "donker" and Lengte >= 185 and Gewicht >= 70 and Gewicht <= 90
    Pimpel = leeftijd_diploma == True and Leeftijd >= 60 and Kaal == "nee" and Bril == "ja" and Snor == "ja" and Haar_kleur == "blond" and Lengte >= 185 and Gewicht >= 70 and Gewicht <= 90
    if groenenwoud == True:
        return print("Je mag op auditie voor de rol van Dominee Groenewoud")
    elif Van_Geelen == True:
        return print("Je mag op auditie voor de rol van Kolonel van Geelen")
    elif Pimpel == True:
        return print("Je mag op auditie voor de rol van Professor Pimpel")
    else:
        return print("Je mag helaas niet op auditie.")
def Vrouw():
    Haar_Lengte = input("Is uw haar langer dan 25 centimeter?")
    Haar_Style = input("Heeft u als haar style een pony?")
    Uiterlijk = input("Wat beoordeeld u uwzelf op schaal van 1 tot 10 op uiterlijk")
    De_Wit = leeftijd_diploma == True and Leeftijd >= 60 and Lengte <= 165 and Gewicht >= 50 and Gewicht <= 70 and Haar_Lengte =="nee" and Haar_Style == "nee"
    Roodhart = leeftijd_diploma == True and Leeftijd >= 18 and Leeftijd <= 28 and Lengte <= 165 and Gewicht >= 50 and Gewicht <= 70 and Haar_Lengte =="ja" and Haar_Style == "nee" and Uiterlijk >= 7 and Uiterlijk <= 10
    Draet = leeftijd_diploma == True and Leeftijd >= 28 and Leeftijd <= 50 and Lengte <= 165 and Gewicht >= 50 and Gewicht <= 70 and Haar_Lengte =="ja" and Haar_Style == "nee" and Uiterlijk >= 7 and Uiterlijk <= 10
    if De_Wit == True:
        return print("Je mag op auditie voor de rol van Mevrouw de Wit")
    elif Roodhart == True:
        return print("Je mag op auditie voor de rol van Rosa Roodhart")
    elif Draet == True:
        return print("Je mag op auditie voor de rol van Mevrouw Blaauw van Draet")
    else:
        return print("Je mag helaas niet op auditie.")
if Geslacht == "M":
    Man()
else:
    Vrouw()
