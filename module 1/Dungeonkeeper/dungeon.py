import time, math
import random
import operator

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}

player_attack = 1
player_defense = 0
player_health = 3
sleutel = 0
som_nummer1 = 1#random.randint(10, 25)
som_nummer2 = 1#random.randint(-5, 75)
op = random.choice(list(operations.keys()))
som_antwoord = operations[op](som_nummer1, som_nummer2)

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [kamer 2] === #
print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
print('Het standbeeld heeft een sleutel vast.')
print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
print(f'Daarboven zie je een som staan {som_nummer1}{op}{som_nummer2} =?')
antwoord = int(input('Wat toets je in?'))

if antwoord == som_antwoord:
    print('Het stadbeeld laat de sleutel vallen en je pakt het op')
    sleutel += 1
else:
    print('Er gebeurt niets....')

print('Je zie een deur achter het standbeeld.')
print('')
time.sleep(1)

# === [kamer 3] === #
items = ['schild', 'zwaard']
chosen_item = random.choice(items)

if chosen_item == 'zwaard':
    player_attack += 2
elif chosen_item == 'schild':
    player_defense += 1

print('Je duwt hem open en stap een hele lange kamer binnen.')
print(f'In deze kamer staat een tafel met daarop een {chosen_item}.')
print(f'Je pakt het {chosen_item} op en houd het bij je.')
print('Op naar de volgende deur.')
print('')
time.sleep(1)

# === [kamer 4] === #
zombie_attack = 1
zombie_defense = 0
zombie_health = 2
print(f'Dapper met je nieuwe {chosen_item} loop je de kamer binnen.')
print('Je loopt tegen een zombie aan.')

zombie_hit_damage = (zombie_attack - player_defense)
if zombie_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
else:
    zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
    
    player_hit_damage = (player_attack - zombie_defense)
    player_attack_amount = math.ceil(zombie_health / player_hit_damage)

    if player_attack_amount < zombie_attack_amount:
        player_health = player_health - player_attack_amount * zombie_attack
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()
print('')
time.sleep(1)

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
time.sleep(1)

if sleutel == 1:
    print('Je hebt de sleutel!')
    print('Je opent de kist en bent verbaast met wat er in zit!')
    exit()
else:
    print('Hoe moet je de kist open maken zonder sleutel!')
    print('De kist gaat niet open')
    print('Game Over.')
    exit()