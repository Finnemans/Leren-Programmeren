from fruitmand import fruitmand
gewichtmand = 0

for fruit in fruitmand:
        gewichtmand += fruit['weight']

print(gewichtmand)

fruitmand.append({
    'name': 'watermeloen',
    'weight': 2500,
    'color': 'green',
    'round': True
})

gewichtmand = 0
for fruit in fruitmand:
        gewichtmand += fruit['weight']

print(gewichtmand)