import time
import random
import operator

# Speler initiële waarden
player_attack = 1
player_defense = 0
player_health = 3
sleutel = 0
rupee = 0

# Functie voor eenvoudige gevechten
def fight_enemy(player_attack, player_defense, player_health, enemy_attack, enemy_defense, enemy_health):
    player_hit_damage = max(0, player_attack - enemy_defense)
    enemy_hit_damage = max(0, enemy_attack - player_defense)

    if player_hit_damage == 0:
        print('Je kunt geen schade toebrengen aan de vijand.')
    else:
        print(f'Je doet {player_hit_damage} schade aan de vijand.')

    if enemy_hit_damage == 0:
        print('De vijand kan jou geen schade toebrengen.')
    else:
        player_health -= enemy_hit_damage
        print(f'De vijand doet {enemy_hit_damage} schade. Je health is nu {player_health}.')

    if enemy_health <= player_hit_damage:
        print('Je hebt de vijand verslagen!')
    elif player_health <= 0:
        print('Je hebt verloren! Game over.')
        exit()

    return player_health

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [kamer 7] === #
print('Je komt in kamer 7.')
# Kans van 1 op 10 dat er geen rupee ligt
if random.randint(1, 10) == 1:
    print('De betovering van de wizard is sterk, er ligt geen rupee in deze kamer.')
else:
    print('Kijk nou! Er ligt hier een rupee.')
    rupee += 1
time.sleep(1)

print('Je ziet twee uitgangen:')
print('1. Rechtdoor naar kamer 2')
print('2. Rechtsaf naar kamer 8 (gokmachine)')

# Keuze maken tussen kamer 2 of kamer 8
while True:
    keuze = input('Kies je voor rechtdoor naar kamer 2 of rechtsaf naar kamer 8? (2/8): ')
    if keuze in ['2', '8']:
        break
    else:
        print('Ongeldige keuze. Kies 2 of 8.')

if keuze == '2':
    # Ga naar kamer 2
    print('Je besluit rechtdoor te gaan en opent de deur naar kamer 2.')
    time.sleep(1)

    # === [kamer 2] === #
    som_nummer1 = random.randint(10, 25)
    som_nummer2 = random.randint(-5, 75)
    operations = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    op = random.choice(list(operations.keys()))
    som_antwoord = operations[op](som_nummer1, som_nummer2)

    print(f'Je ziet een groot standbeeld met een puzzel: {som_nummer1} {op} {som_nummer2} =?')
    antwoord = int(input('Wat is je antwoord? '))

    if antwoord == som_antwoord:
        print('Het standbeeld laat een rupee vallen. Je pakt het op.')
        rupee += 1
    else:
        print('Er gebeurt niets...')
    
    time.sleep(1)
    print('Je ziet twee deuren: naar kamer 6 of kamer 8.')
    keuze = input('Kies je voor kamer 6 of kamer 8? (6/8): ')

    if keuze == '6':
        # === [kamer 6] === #
        print('Je opent de deur naar kamer 6. Het is donker en je hoort gegrom.')
        time.sleep(1)

        print('Een monster valt aan!')
        enemy_attack = 1
        enemy_defense = 0
        enemy_health = 2

        player_health = fight_enemy(player_attack, player_defense, player_health, enemy_attack, enemy_defense, enemy_health)
        print('Na de strijd zie je een deur naar kamer 8.')
        time.sleep(1)

    elif keuze == '8':
        # === [kamer 8] === #
        print('Je opent de deur naar kamer 8 en ziet een gokmachine.')
        print('Wil je een gokje wagen?')

        gokken = input('Wil je gokken? (ja/nee): ').lower()
        if gokken == 'ja':
            dobbel1 = random.randint(1, 6)
            dobbel2 = random.randint(1, 6)
            totaal = dobbel1 + dobbel2

            print(f'Je hebt {dobbel1} en {dobbel2} gegooid. Totaal: {totaal}.')

            if totaal > 7:
                rupee *= 2
                print(f'Gefeliciteerd! Je hebt nu {rupee} rupees.')
            elif totaal < 7:
                player_health -= 1
                print(f'Je verliest 1 health. Je health is nu {player_health}.')
                if player_health <= 0:
                    print('Je health is 0. Game over.')
                    exit()
            else:
                rupee += 1
                player_health += 4
                print(f'Je hebt precies 7 gegooid! Je krijgt 1 rupee en 4 health. Je hebt nu {rupee} rupee(s) en {player_health} health.')

        # Na kamer 8 moet je door naar kamer 9
        print('Je opent de deur en komt in kamer 9.')
        time.sleep(1)

        # === [kamer 9] === #
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

# === [kamer 3] === #
items = ['schild', 'zwaard', 'sleutel']

print('Een goblin staat nu in kamer 3 met een groter assortiment.')
print(f'Je hebt {rupee} rupee(s).')

# Check hoeveel rupees de speler heeft
if rupee >= 3:
    print('1. Koop een zwaard voor 1 rupee\n2. Koop een schild voor 1 rupee\n3. Koop een sleutel voor 2 rupees\n4. Koop niets')
elif rupee == 2:
    print('1. Koop een zwaard voor 1 rupee\n2. Koop een schild voor 1 rupee\n3. Koop een sleutel voor 2 rupees (alle rupees)\n4. Koop niets')
elif rupee == 1:
    print('1. Koop een zwaard voor 1 rupee\n2. Koop een schild voor 1 rupee\n3. Koop niets')
else:
    print('Je hebt geen rupees om iets te kopen.')

keuze = input('Maak je keuze (1/2/3/4): ')

if keuze == '1' and rupee >= 1:
    player_attack += 2
    rupee -= 1
    print('Je hebt een zwaard gekocht. Je aanval is nu hoger.')
elif keuze == '2' and rupee >= 1:
    player_defense += 1
    rupee -= 1
    print('Je hebt een schild gekocht. Je verdediging is nu hoger.')
elif keuze == '3' and rupee >= 2:
    sleutel += 1
    rupee -= 2
    print('Je hebt de sleutel gekocht! Nu kun je de schatkist openen.')
elif keuze == '4':
    print('Je besluit niets te kopen.')
time.sleep(1)
print(' ')
# === [kamer 4] === #
print('Je komt een grote zombie tegen.')
enemy_attack = 2
enemy_defense = 0
enemy_health = 3

player_health = fight_enemy(player_attack, player_defense, player_health, enemy_attack, enemy_defense, enemy_health)
print(' ')

# === [kamer 5] === #
print('Je komt een schatkist tegen.')
if sleutel == 1:
    print('Je opent de kist!')
else:
    print('Je hebt geen sleutel. Game over.')