import random

namen = []
while len(namen) < 3:
    naam = input("Voer uw naam in: ")
    if naam not in namen:
        namen.append(naam)
    else:
        print("Deze naam bestaat al, probeer opnieuw.")

while True:
    keuze = input("Wil je nog een naam toevoegen? (ja/nee): ").lower()
    if keuze == "ja":
        naam = input("Voer een unieke naam in: ")
        if naam not in namen:
            namen.append(naam)
        else:
            print("Deze naam bestaat al.")
    elif keuze == "nee":
        break
    else:
        print("Ongeldige invoer, typ 'ja' of 'nee'.")

lootjes = namen.copy()
while True:
    random.shuffle(lootjes)
    if all(namen[i] != lootjes[i] for i in range(len(namen))):
        break

while True:
    vraag = input("Voer je naam in om te zien wie je hebt (typq 'stop' om te stoppen): ")
    if vraag == "stop":
        break
    elif vraag in namen:
        index = namen.index(vraag)
        print(f"{vraag} -> {lootjes[index]}!")
    else:
        print("Naam niet gevonden, probeer opnieuw.")