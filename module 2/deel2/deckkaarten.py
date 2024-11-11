import random

kleuren = ["harten", "klaveren", "schoppen", "ruiten"]
waardes = [str(i) for i in range(2, 11)] + ["boer", "vrouw", "heer", "aas"]


deck = [f"{kleur} {waarde}" for kleur in kleuren for waarde in waardes] + ["joker", "joker"]

random.shuffle(deck)

bovenste_kaarten = deck[:7]
overige_kaarten = deck[7:]

print("Bovenste 7 kaarten:")
for i in bovenste_kaarten:
    print(i)
print(' ')

print(f"deck({len(overige_kaarten)} kaarten): {overige_kaarten}")