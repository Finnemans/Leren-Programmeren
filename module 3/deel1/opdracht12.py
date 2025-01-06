from fruitmand import fruitmand
thisdict = {
    "yellow": "gele",
    "green": "groene",
    "orange": "oranje",
    "red": "rode",
    "brown": "bruine",
    "purple": "paarse",
    "pink": "roze",
    "black": "zwarte"
}
langstenaam = fruitmand[0]
for fruit in fruitmand:
    if len(fruit['name']) > len(langstenaam['name']):
        langstenaam = fruit

kleur = langstenaam['color']
kleur = (thisdict[kleur])
gewicht = langstenaam['weight'] / 1000

print(f'De {langstenaam['name']} ({len(langstenaam['name'])} letters) heeft een {kleur} kleur en een gewicht van {gewicht}kg')