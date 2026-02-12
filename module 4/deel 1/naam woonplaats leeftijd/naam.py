def vraag_naam_en_leeftijd():
    naam = input("Wat is je naam? ")
    woonplaats = input("Wat is je woonplaats? ")
    leeftijd = int(input("Wat is je leeftijd? "))
    return {"name": naam, "city": woonplaats, "age": leeftijd}

def verzamel_personen():
    personen = [] #lijst waar alles in kan
    while True:
        keuze = input("Toets enter om door te gaan of 'stop' om te printen: ")
        if keuze.lower() == 'stop':
            break
        persoon = vraag_naam_en_leeftijd() #slaat op als persoon
        personen.append(persoon) #doet t persoon in de lijst
    return personen

personen_lijst = verzamel_personen()

for persoon in personen_lijst:
    print(f"{persoon['name']}, die in {persoon['city']} woont, is {persoon['age']} jaar")