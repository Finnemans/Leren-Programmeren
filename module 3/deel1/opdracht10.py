from fruitmand import fruitmand

sorted_fruitmand = sorted(fruitmand, key=lambda x: x['weight'])[::-1]

for fruit in sorted_fruitmand:
    gewicht = fruit['weight'] / 1000
    print(f'{fruit['name']}: {gewicht} kg')