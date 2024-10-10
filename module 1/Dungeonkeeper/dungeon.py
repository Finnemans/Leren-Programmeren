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
print('er ligt hier een rupee.')
rupee += 1
time.sleep(1)

# === [kamer 2] === #
print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
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
print('De linker deur leidt naar kamer 6, de rechter naar kamer 3.')
print('')
time.sleep(1)

# Keuze maken tussen kamer 6 en kamer 3
keuze = input('Kies je voor kamer 6 of kamer 3? (6/3): ')

if keuze == '6':
    # === [kamer 6] === #
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

    print('Na de strijd zie je een deur en gaat kamer 3 binnen...')
    time.sleep(1)

elif keuze == '3':
    print('Je opent de deur naar kamer 3.')
    time.sleep(1)

# === [kamer 3] === #
items = ['schild', 'zwaard']
chosen_item = random.choice(items)
print('Je duwt de deur open en stapt een lange kamer binnen.')

print('Een goblin staat voor je met een tafel vol wapens.')
print('Hij zegt: "Welkom! Ik verkoop zwaarden en schilden voor 1 rupee elk."')
print('Wat wil je doen?')
print('1. Koop een zwaard voor 1 rupee')
print('2. Koop een schild voor 1 rupee')
print('3. Koop niets')
    
while True:
        keuze = input('Maak een keuze (1/2/3): ')
        if keuze in ['1', '2', '3']:
            break
        else:
            print('Ongeldige keuze. Kies 1, 2 of 3.')
    
if keuze == '1':
        if rupee >= 1:
            player_attack += 2
            rupee -= 1
            print('Je hebt een zwaard gekocht! Je aanval is nu verhoogd.')
            print(f'Je hebt nog {rupee} rupee(s).')
        else:
            print('Je hebt niet genoeg rupees om een zwaard te kopen.')
elif keuze == '2':
        if rupee >= 1:
            player_defense += 1
            rupee -= 1
            print('Je hebt een schild gekocht! Je verdediging is nu verhoogd.')
            print(f'Je hebt nog {rupee} rupee(s).')
        else:
            print('Je hebt niet genoeg rupees om een schild te kopen.')
elif keuze == '3':
        print('Je besluit niets te kopen.')

print('')
time.sleep(1)

# === [kamer 4] === #
print('Je loopt tegen een zombie aan.')
print('Deze zombie is veel groter dan de vorige!')
print(f'Gelukkig heb je je {chosen_item}.')

enemy_attack = 2
enemy_defense = 0
enemy_health = 3

# Voer het gevecht uit met de gekozen vijand
player_health = fight_enemy(player_attack, player_defense, player_health, enemy_attack, enemy_defense, enemy_health)
print('')
time.sleep(1)

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
time.sleep(1)

if sleutel == 1:
    print('Je hebt de sleutel!')
    print('Je opent de kist en bent verbaasd met wat er in zit!')
else:
    print('Hoe moet je de kist openmaken zonder sleutel?!')
    print('De kist gaat niet open.')
    print('Game Over.')
