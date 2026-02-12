import random

def genereer_wachtwoord():
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
        return genereer_wachtwoord()
##aan elkaar
    return "".join(wachtwoord)

print(genereer_wachtwoord())