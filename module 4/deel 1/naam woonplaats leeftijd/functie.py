from termcolor import colored
def vraag_naam_en_leeftijd():
    naam = input("Wat is je naam? ")
    woonplaats = input("Wat is je woonplaats? ")
    leeftijd = int(input("Wat is je leeftijd? "))
    return {"name": naam, "city": woonplaats, "age": leeftijd}

def check_volwassen(leeftijd):
    if leeftijd >= 18:
        leeftijd -= 18
        return colored(f"al {leeftijd} jaar", "red")
    else:
        return colored("nog niet", "red")

def verzamel_personen():
    personen = []  # lijst waar alles in kan
    while True:
        keuze = input("Toets enter om door te gaan of 'stop' om te printen: ")
        if keuze.lower() == 'stop':
            break
        persoon = vraag_naam_en_leeftijd()  # slaat op als persoon
        personen.append(persoon)  # doet het persoon in lijst
    return personen