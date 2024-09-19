getal_1 = int(input("eerste getal: "))
getal_2 = int(input("tweede getal: "))


if getal_2 == 0:
    print("Kan niet delen door 0")
else:
    resultaat = getal_1 / getal_2
    print (f"{getal_1} gedeeld door {getal_2} is gelijk aan {resultaat}".format(getal_1, getal_2, resultaat))
    

def vraag_getal(aantal):
    antwoord = input("Voer het "+antwoord+" getal in: ")
    getal = int(aantal)
    return getal

def deel_getallen(a, b):
    antwoord = print(a / b)
    return antwoord