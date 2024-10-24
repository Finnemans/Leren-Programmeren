import random

kleuren = ('oranje', 'blauw', 'groen', 'bruin')
aantal = int(input("Hoeveel M&M's wil je aan de zak toevoegen? "))
zak = []

for x in range(aantal):
    zak.append(random.choice(kleuren))

print(f"Inhoud van de zak met M&M's: {zak}")
