import random

kleuren = ['rood', 'blauw', 'groen', 'geel', 'bruin']

aantal = int(input("Hoeveel M&M's wil je in de zak stoppen? "))

zak = {}

for i in range(aantal):
    kleur = random.choice(kleuren)
    if kleur in zak:
        zak[kleur] += 1
    else:
        zak[kleur] = 1

print("Inhoud van de zak M&M's:")
for kleur, aantal in zak.items():
    print(f"{kleur}: {aantal}")