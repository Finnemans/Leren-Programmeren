from fruitmand import fruitmand
import random
aantal = int(input('Voer een getal in: '))

for x in range(aantal):
    randfruit = random.choice(fruitmand)
    print(randfruit['name'])