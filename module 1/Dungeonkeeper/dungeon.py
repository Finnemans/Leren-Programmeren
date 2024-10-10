import time
import math
import random
import operator

def fight_enemy(player_attack, player_defense, player_health, enemy_attack, enemy_defense, enemy_health):
    enemy_hit_damage = (enemy_attack - player_defense)
    
    if enemy_hit_damage <= 0:
        print('Jij hebt een te goede verdediging voor de vijand, hij kan je geen schade doen.')
        enemy_attack_amount = 0  # Geen aanvallen van de vijand
    else:
        enemy_attack_amount = math.ceil(player_health / enemy_hit_damage)

    # Bereken de schade die de speler kan toebrengen
    player_hit_damage = (player_attack - enemy_defense)
    
    if player_hit_damage <= 0:
        print('Je kunt geen schade toebrengen aan de vijand.')
        player_attack_amount = 0  # Geen aanvallen van de speler
    else:
        player_attack_amount = math.ceil(enemy_health / player_hit_damage)

    if player_attack_amount < enemy_attack_amount and player_health > 0:
        player_health -= enemy_attack_amount * enemy_attack
        print(f'In {player_attack_amount} rondes versla je de vijand.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de vijand te sterk voor je.')
        print('Game over.')
        exit()

    return player_health

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}

# Speler initiële waarden
player_attack = 1
player_defense = 0
player_health = 3
sleutel = 0
rupee = 0

som_nummer1 = random.randint(10, 25)
som_nummer2 = random.randint(-5, 75)
op = random.choice(list(operations.keys()))
som_antwoord = operations[op](som_nummer1, som_nummer2)

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [kamer 7] === #
print('Kijk nou!')
print('Er ligt hier een rupee.')
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
    print('')
    time.sleep(1)

    # === [kamer 2] === #
    print('Je stapt door de deur en ziet een groot standbeeld voor je.')
    print('Het standbeeld heeft een sleutel vast.')
    print('Op zijn borst zit een numpad met de toetsen 9 t/m 0.')
    print(f'Daarboven zie je een som staan {som_nummer1} {op} {som_nummer2} =?')
    antwoord = int(input('Wat toets je in? '))

    if antwoord == som_antwoord:
        print('Het standbeeld laat de sleutel vallen en je pakt het op.')
        sleutel += 1
    else:
        print('Er gebeurt niets....')

    print('Je ziet een deur achter het standbeeld.')
    print('')
    time.sleep(1)

    print('Je ziet twee deuren achter het standbeeld.')
    print('De linker deur leidt naar kamer 6, de rechter naar kamer 8.')
    print('')
    time.sleep(1)

    # Keuze maken tussen kamer 6 en kamer 8 vanuit kamer 2
    keuze = input('Kies je voor kamer 6 of kamer 8? (6/8): ')

    if keuze == '6':
        # Ga naar kamer 6
        print('Je opent de deur naar kamer 6.')
        print('Deze kamer is donker en je hoort een gegrom.')
        time.sleep(1)

        enemy_attack = 1
        enemy_defense = 0
        enemy_health = 2

        print('Je hebt geen wapens of schild om je te helpen. Je gaat de strijd in met je basisvaardigheden.')
        time.sleep(1)

        player_health = fight_enemy(player_attack, player_defense, player_health, enemy_attack, enemy_defense, enemy_health)
        print('')
        time.sleep(1)

        # Ga naar kamer 8 vanuit kamer 6
        print('Na de strijd zie je een deur die naar kamer 8 leidt...')
        time.sleep(1)
        print('Je opent de deur naar kamer 8...')
        time.sleep(1)

        # === [kamer 8] === #
        print('Je komt een kamer binnen en ziet een fel verlichte gokmachine staan.')
        print('Er staat: "Wil je een gokje wagen?"')
        print('Als je wint, verdubbel je je rupees. Als je verliest, verlies je 1 health.')
        print('Gooi je 7? Dan krijg je 1 rupee en 4 health!')

        keuze = input('Wil je gokken? (ja/nee): ').lower()

        if keuze == 'ja':
            # Twee zeszijdige dobbelstenen gooien
            dobbel1 = random.randint(1, 6)
            dobbel2 = random.randint(1, 6)
            totaal = dobbel1 + dobbel2

            print(f'Je hebt {dobbel1} en {dobbel2} gegooid. Het totaal is {totaal}.')

            if totaal > 7:
                rupee *= 2
                print(f'Gefeliciteerd! Je hebt gewonnen. Je hebt nu {rupee} rupees.')
            elif totaal < 7:
                player_health -= 1
                print(f'Helaas, je hebt verloren en verliest 1 health. Je health is nu {player_health}.')
                if player_health <= 0:
                    print('Je health is 0. Je hebt het spel verloren.')
                    exit()
            else:  # totaal == 7
                rupee += 1
                player_health += 4
                print('Geweldig! Je hebt precies 7 gegooid.')
                print(f'Je krijgt 1 rupee en 4 health. Je hebt nu {rupee} rupee(s) en {player_health} health.')

        print('Je gaat door naar kamer 3...')
        time.sleep(1)

    elif keuze == '8':
        # Ga naar kamer 8 vanuit kamer 2
        print('Je opent de deur naar kamer 8...')
        time.sleep(1)

        # === [kamer 8] === #
        print('Je komt een kamer binnen en ziet een fel verlichte gokmachine staan.')
        print('Er staat: "Wil je een gokje wagen?"')
        print('Als je wint, verdubbel je je rupees. Als je verliest, verlies je 1 health.')
        print('Gooi je 7? Dan krijg je 1 rupee en 4 health!')

        keuze = input('Wil je gokken? (ja/nee): ').lower()

        if keuze == 'ja':
            # Twee zeszijdige dobbelstenen gooien
            dobbel1 = random.randint(1, 6)
            dobbel2 = random.randint(1, 6)
            totaal = dobbel1 + dobbel2

            print(f'Je hebt {dobbel1} en {dobbel2} gegooid. Het totaal is {totaal}.')

            if totaal > 7:
                rupee *= 2
                print(f'Gefeliciteerd! Je hebt gewonnen. Je hebt nu {rupee} rupees.')
            elif totaal < 7:
                player_health -= 1
                print(f'Helaas, je hebt verloren en verliest 1 health. Je health is nu {player_health}.')
                if player_health <= 0:
                    print('Je health is 0. Je hebt het spel verloren.')
                    exit()
            else:  # totaal == 7
                rupee += 1
                player_health += 4
                print('Geweldig! Je hebt precies 7 gegooid.')
                print(f'Je krijgt 1 rupee en 4 health. Je hebt nu {rupee} rupee(s) en {player_health} health.')

        print('Je gaat door naar kamer 3...')
        time.sleep(1)

# === [kamer 3] === #
items = ['schild', 'zwaard']

print('Een goblin staat voor je met een tafel vol wapens.')
print('Hij kijkt je aan en lijkt te weten hoeveel rupees je hebt.')
print('Hij zegt: "Ik verkoop zwaarden en schilden. Wat wil je kopen?"')

while True:
    if rupee >= 2:
        print('1. Koop een zwaard voor 1 rupee')
        print('2. Koop een schild voor 1 rupee')
        print('3. Koop beide voor 2 rupees')
        print('4. Koop niets')
    elif rupee == 1:
        print('1. Koop een zwaard voor 1 rupee')
        print('2. Koop een schild voor 1 rupee')
        print('3. Koop niets')
    else:
        print('Je hebt niet genoeg rupees om iets te kopen.')
        break

    keuze = input('Maak een keuze (1/2/3/4): ')
    if keuze == '1' and rupee >= 1:
        player_attack += 2
        rupee -= 1
        print('Je hebt een zwaard gekocht! Je aanval is nu verhoogd.')
    elif keuze == '2' and rupee >= 1:
        player_defense += 1
        rupee -= 1
        print('Je hebt een schild gekocht! Je verdediging is nu verhoogd.')
    elif keuze == '3' and rupee >= 2:
        player_attack += 2
        player_defense += 1
        rupee -= 2
        print('Je hebt zowel een zwaard als een schild gekocht!')
    elif keuze == '4':
        print('Je besluit niets te kopen.')
        break
    else:
        print('Ongeldige keuze of niet genoeg rupees.')

print('Je verlaat de kamer en gaat door naar de volgende...')

# === [kamer 4] === #
print('Je loopt tegen een zombie aan.')
print('Deze zombie is veel groter dan de vorige!')

enemy_attack = 2
enemy_defense = 0
enemy_health = 3

# Voer het gevecht uit met de gekozen vijand
player_health = fight_enemy(player_attack, player_defense, player_health, enemy_attack, enemy_defense, enemy_health)
print('')
time.sleep(1)

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
time.sleep(1)
print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
time.sleep(1)

if sleutel == 1:
    print('Je hebt de sleutel!')
    time.sleep(1)
    print('Je opent de kist en bent verbaasd met wat er in zit!')
else:
    print('Hoe moet je de kist openmaken zonder sleutel?!')
    time.sleep(1)
    print('De kist gaat niet open.')
    print('Game Over.')
