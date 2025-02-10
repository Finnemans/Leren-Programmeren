import time
import random
import operator

player_attack = 1
player_defense = 0
player_health = 3
sleutel = 0
rupee = 0
zwaard = False
schild = False


def fight_enemy(player_attack, player_defense, player_health, enemy_attack, enemy_defense, enemy_health):
    player_hit_damage = max(0, player_attack - enemy_defense)
    enemy_hit_damage = max(0, enemy_attack - player_defense)

    while player_health > 0 and enemy_health > 0:
        if player_hit_damage > 0:
            print(f"Je doet {player_hit_damage} schade aan de vijand.")
            enemy_health -= player_hit_damage
        else:
            print("Je kunt geen schade toebrengen aan de vijand.")

        if enemy_health <= 0:
            print("Je hebt de vijand verslagen!")
            break

        if enemy_hit_damage > 0:
            print(f"De vijand doet {enemy_hit_damage} schade aan jou.")
            player_health -= enemy_hit_damage
            print(f"Je gezondheid is nu {player_health}.")
        else:
            print("De vijand kan jou geen schade toebrengen.")

        if player_health <= 0:
            print("Je bent verslagen! Game over.")
            break

    return player_health

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [kamer 7] === #
print('Je komt in kamer 7.')

if random.randint(1, 10) == 1:
    print('De betovering van de wizard is sterk, er ligt geen rupee in deze kamer.')
else:
    print('Kijk nou! Er ligt hier een rupee.')
    rupee += 1
time.sleep(1)

print('Je ziet twee uitgangen:')
print('1. Rechtdoor naar kamer 2')
print('2. Rechtsaf naar kamer 8 (gokmachine)')

while True:
    keuze = input('Kies je voor rechtdoor naar kamer 2 of rechtsaf naar kamer 8? (2/8): ')
    if keuze in ['2', '8']:
        break
    else:
        print('Ongeldige keuze. Kies 2 of 8.')

if keuze == '2':
    print('Je besluit rechtdoor te gaan en opent de deur naar kamer 2.')
    time.sleep(1)

    # === [kamer 2] === #
    som_nummer1 = random.randint(10, 25)
    som_nummer2 = random.randint(-5, 75)

    operatoren = [
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul)
    ]

    op, functie = random.choice(operatoren)

    som_antwoord = functie(som_nummer1, som_nummer2)

    print(f'Je ziet een groot standbeeld met een puzzel: {som_nummer1} {op} {som_nummer2} = ?')
    antwoord = int(input('Wat is je antwoord? '))

    if antwoord == som_antwoord:
        print('Het standbeeld laat een rupee vallen. Je pakt het op.')
        rupee += 1
    else:
        print('Er gebeurt niets...')
    
    time.sleep(1)
    print('Je ziet twee deuren: naar kamer 6 of kamer 8.')
    while True:
        keuze = input('Kies je voor kamer 6 of kamer 8? (6/8): ')
        if keuze in ['6','8']:
            break
        else:
            print('Ongeldige keuze. Kies 6 of 8.')

    if keuze == '6':
        # === [kamer 6] === #
        print('Je opent de deur naar kamer 6. Het is donker en je hoort gegrom.')
        time.sleep(1)

        print('Een monster valt aan!')
        enemy_attack = 1
        enemy_defense = 0
        enemy_health = 2

        player_health = fight_enemy(player_attack, player_defense, player_health, enemy_attack, enemy_defense, enemy_health)

        if player_health > 0:
            print(f"Gefeliciteerd! Je hebt overleefd met {player_health} gezondheid.")
        else:
            print("Helaas, je bent verslagen.")
       
        print('Na de strijd zie je een deur naar kamer 8 of kamer 3.')
        time.sleep(1)
    while True:
        keuze = input('Kies je om door te gaan naar kamer 8 of kamer 3? (8/3): ')
        if keuze in ['8', '3']:
            break
        else:
            print('Ongeldige keuze. Kies 8 of 3.')
    if keuze == '8':
        print('Je opent de deur naar kamer 8...')
        time.sleep(1)
    else:
        print('Je opent de deur naar kamer 3...')
        time.sleep(1)


# === [kamer 8] === #
if keuze == '8':
    print('Je komt een kamer binnen en ziet een fel verlichte gokmachine staan.')
    print('Er staat: "Wil je een gokje wagen?"')
    print('Als je wint, verdubbel je je rupees. Als je verliest, verlies je 1 health.')
    print('Gooi je 7? Dan krijg je 1 rupee en 4 health!')

    keuze = input('Wil je gokken? (ja/nee): ').lower()

    if keuze == 'ja':
        dobbel1 = random.randint(1, 6)
        dobbel2 = random.randint(1, 6)
        totaal = dobbel1 + dobbel2

        print(f'Je hebt {dobbel1} en {dobbel2} gegooid. Het totaal is {totaal}.')

        if totaal > 7:
            rupee += 1
            print(f'Gefeliciteerd! Je hebt gewonnen. Je hebt nu {rupee} rupees.')
        elif totaal < 7:
            player_health -= 1
            print(f'Helaas, je hebt verloren en verliest 1 health. Je health is nu {player_health}.')
            if player_health <= 0:
                print('Je health is 0. Je hebt het spel verloren.')
                exit()
        else:
            rupee += 1
            player_health += 4
            print('Geweldig! Je hebt precies 7 gegooid.')
            print(f'Je krijgt 1 rupee en 4 health. Je hebt nu {rupee} rupee(s) en {player_health} health.')

    time.sleep(1)
    print(' ')
    print('Je ziet twee deuren:')

    while True:
        keuze = input('Kies je voor kamer 3 of kamer 9? (3/9): ')
        if keuze in ['3', '9']:
            break
        else:
            print('Ongeldige keuze. Kies 3 of 9.')

    if keuze == '3':
        print('Je opent de deur naar kamer 3...')
        time.sleep(1)
    else:
        print('Je opent de deur naar kamer 9...')
        time.sleep(1)
        print(' ')

# === [kamer 9] === #
if keuze == '9':
    print('Je voelt een vreemde betovering in de lucht...')
    betovering = random.choice(['defense', 'health'])
    if betovering == 'defense':
        player_defense += 1
        print('Je hebt 1 extra verdediging gekregen!')
    else:
        player_health += 2
        print('Je hebt 2 extra health gekregen!')

    time.sleep(1)
    print('Na de betovering loop je verder naar kamer 3...')
    time.sleep(1)
    print(' ')

# === [kamer 3] === #
print('In kamer 3 staat een goblin met een groter assortiment.')

while rupee >= 1:
    print(f"Je hebt {rupee} rupee(s).")

    keuzes = []
    if not zwaard:
        print("1. Koop een zwaard (+2 aanval, 1 rupee)")
        keuzes.append('1')
    if not schild:
        print("2. Koop een schild (+1 verdediging, 1 rupee)")
        keuzes.append('2')
    if sleutel == 0:
        print("3. Koop een sleutel (+1 sleutel, 1 rupee)")
        keuzes.append('3')
    print("4. Koop niets")
    keuzes.append('4')

    keuze = input(f"Maak je keuze ({'/'.join(keuzes)}): ")

    if keuze == '1' and '1' in keuzes:
        player_attack += 2
        rupee -= 1
        zwaard = True
        print("Je hebt een zwaard gekocht. Je aanval is nu hoger.")
    elif keuze == '2' and '2' in keuzes:
        player_defense += 1
        rupee -= 1
        schild = True
        print("Je hebt een schild gekocht. Je verdediging is nu hoger.")
    elif keuze == '3' and '3' in keuzes:
        sleutel += 1
        rupee -= 1
        print("Je hebt de sleutel gekocht! Nu kun je een schatkist openen.")
    elif keuze == '4':
        print("Je besluit niets te kopen.")
        break
    else:
        print("Ongeldige keuze of niet genoeg rupees.")

    if rupee >= 1:
        print("Je hebt nog steeds rupees over. Je kunt nog iets kopen.")
    else:
        print("Je hebt geen rupees meer. De winkel sluit.")


    time.sleep(1)


# === [kamer 4] === #
print(' ')
print('Je komt een grote zombie tegen.')
time.sleep(1)
enemy_attack = 2
enemy_defense = 0
enemy_health = 3

player_health = fight_enemy(player_attack, player_defense, player_health, enemy_attack, enemy_defense, enemy_health)

if player_health > 0:
    print(f"Gefeliciteerd! Je hebt overleefd met {player_health} gezondheid.")
else:
    print("Helaas, je bent verslagen.")
    
time.sleep(1)
print(' ')

# === [kamer 5] === #
print('Je komt een schatkist tegen.')
time.sleep(1)
if sleutel == 1:
    print('Je opent de kist!')
else:
    print('Je hebt geen sleutel. Game over.')
