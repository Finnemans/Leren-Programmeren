from fruitmand import fruitmand
kleuren = []
for fruit in fruitmand:
    if fruit['name'] == 'druif':
        fruitmand.remove(fruit)

for fruit in fruitmand:
    if (fruit['color']) not in kleuren:
        kleuren.append(fruit['color'])
print(kleuren)