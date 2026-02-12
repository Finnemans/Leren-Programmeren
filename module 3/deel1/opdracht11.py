from fruitmand import fruitmand
round = 0
notround = 0
list = []
for fruit in fruitmand:
    list.append(fruit['color'])
while True:
    kleur = input('Kies een kleur van het fruit: yellow, green, orange, red, brown, pink, purple, black ')
    if kleur in list:
        break
    else:
        print(f'De kleur {kleur} zit er niet in de fruitmand')

for fruit in fruitmand:
    if fruit['color'] == kleur:
        if fruit['round'] == True:
            round += 1
        else:
            notround += 1

if round > notround:
    round - notround
    print(f'Er zijn {round} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}')
elif round < notround:
    notround - round
    print(f'Er zijn {notround} minder. ronde vruchten dan niet ronde vruchten in de kleur {kleur}')
elif round == notround:
    print(f'“Er zijn {round} ronde vruchten en {notround} niet ronde vruchten in de kleur {kleur}”')