# password 24 karakters lang!
# Random 2 tot 6 hoofdletters.
# Een hoofdletter mag niet op de twee middelste posities staan.
## Minimaal 8 kleine letters.
## Het wachtwoord mag niet met een kleine letter eindigen.
# 3 speciale tekens uit de volgende reeks: @ # $ % & _ ?.
## De speciale tekens mogen niet op de eerste of laatste positie staan.
# Random 4 tot 7 cijfers (0 t/m 9).
## Op de eerste 3 posities mag geen cijfer staan
import time, string

def test_wachtwoord(ww) -> bool:
    if len(ww) < 24:
        print('te kort')
        return False
    if not 1 < len(list(filter(lambda a: a in string.ascii_uppercase, list(ww)))) < 7:
        print('aantal hoofdletters klopt niet!')
        return False
    if ww[11] in string.ascii_uppercase or ww[12] in string.ascii_uppercase:
        print('In het midden geen hoofdletters')
        return False
    if len(list(filter(lambda a: a in string.ascii_lowercase, list(ww)))) < 8:
        print('te weinig kleine letters')
        return False
    if ww[-1] in string.ascii_lowercase:
        print('Laatste pos niet juist')
        return False
    if len(list(filter(lambda a: a in '@#$%&_?', list(ww)))) != 3:
        print('te weinig specials')
        return False
    if ww[0] in '@#$%&_?' or ww[-1] in '@#$%&_?':
        print('special op end')
        return False
    if not 3 < len(list(filter(lambda a: a.isdigit(), list(ww)))) < 8:
        print('te weinig getallen')
        return False
    if ww[0].isdigit() or ww[1].isdigit() or ww[2].isdigit():
        print('Eerste drie karakters staat een getal')
        return False
    return True

import random

def get_wachtwoord():
    hoofdletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    kleine_letters = "abcdefghijklmnopqrstuvwxyz"
    cijfers = "0123456789"
    specials = "@#$%&_?"

    wachtwoord = [""] * 24
    bezette_posities = []
##2tot6 hoofdletters
    aantal = random.randint(2, 6)
    while aantal > 0:
        plek = random.randint(0, 23)
        if plek not in [11, 12] and wachtwoord[plek] == "":
            wachtwoord[plek] = random.choice(hoofdletters)
            aantal -= 1
##4tot7 cijfers
    aantal = random.randint(4, 7)
    while aantal > 0:
        plek = random.randint(3, 23)
        if wachtwoord[plek] == "":
            wachtwoord[plek] = random.choice(cijfers)
            aantal -= 1
##3 speciaal tekens tussen tussen 1 en 22
    aantal = 3
    while aantal > 0:
        plek = random.randint(1, 22)
        if wachtwoord[plek] == "":
            wachtwoord[plek] = random.choice(specials)
            aantal -= 1
##invullen met kleine letters
    for i in range(24):
        if wachtwoord[i] == "":
            wachtwoord[i] = random.choice(kleine_letters)

##alles opnieuw tot laatste geen kleine letter is
    if wachtwoord[-1] in kleine_letters:
        return get_wachtwoord()
##aan elkaar
    return "".join(wachtwoord)


# plaats hier de code om minimaal 500 wachtwoorden te testen.
aantal_goede = 0
aantal_foute = 0

for _ in range(500):
    ww = get_wachtwoord()
    if test_wachtwoord(ww):
        aantal_goede += 1
    else:
        print(f"Fout wachtwoord: {ww}")
        aantal_foute += 1

print(f"Totaal geldig: {aantal_goede}")
print(f"Totaal ongeldig: {aantal_foute}")