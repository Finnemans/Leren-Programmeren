from fruitmand import fruitmand

for fruit in fruitmand:
    if fruit['name'] == 'druif':
        fruitmand.remove(fruit)

for fruit in fruitmand:
    print(fruit['color'])
