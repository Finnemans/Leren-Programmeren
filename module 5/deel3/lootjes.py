import random

namen = []
cadeaus = {}

while len(namen) < 3:
    naam = input("Voer uw naam in: ")
    if naam not in namen:
        namen.append(naam)
        cadeaus[naam] = []
        print(f"Voer drie cadeautjes in die {naam} graag wil ontvangen:")
        for i in range(3):
            wens = input(f"  Cadeau {i+1}: ")
            cadeaus[naam].append(wens)
    else:
        print("Deze naam bestaat al, probeer opnieuw.")

while True:
    keuze = input("Wil je nog een naam toevoegen? (ja/nee): ").lower()
    if keuze == "ja":
        naam = input("Voer een unieke naam in: ")
        if naam not in namen:
            namen.append(naam)
            cadeaus[naam] = []
            print(f"Voer drie cadeautjes in die {naam} graag wil ontvangen:")
            for i in range(3):
                wens = input(f"  Cadeau {i+1}: ")
                cadeaus[naam].append(wens)
        else:
            print("Deze naam bestaat al.")
    elif keuze == "nee":
        break
    else:
        print("Ongeldige invoer, typ 'ja' of 'nee'.")

lootjes = namen.copy()
while True:
    random.shuffle(lootjes) 
    probleem = False
    # if all(namen[i] != lootjes[i] for i in range(len(namen))):
    #     break
    for i in range(len(namen)):
        if lootjes[i] == namen[i]:
            probleem = True
            break
    if not probleem:
        break

while True:
    vraag = input("\nVoer je naam in om te zien wie je hebt (typ 'stop' om te stoppen): ")
    if vraag.lower() == "stop":
        break
    elif vraag in namen:
        index = namen.index(vraag)
        getrokken = lootjes[index]
        print(f"{vraag} heeft {getrokken} getrokken.")
        print(f"Wensenlijst van {getrokken}:")
        for i, wens in enumerate(cadeaus[getrokken], start=1):
            print(f"{i}. {wens}")
    else:
        print("Naam niet gevonden.")