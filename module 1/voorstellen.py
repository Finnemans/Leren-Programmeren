naam = input("Wat is je naam? ")
leeftijd = int(input("Hoe oud ben je? "))
gender = input("Ben je een A) een jonge of B) een meisje? ").lower()
kleur = input("Wat is je favoriete kleur? ")
getal = int(input("Wat is je favoriete getal? "))
leeftijdn = abs(leeftijd-getal)
gender1 = 'haar' if gender == 'b' else 'zijn'

print("")
print("Mag ik je voorstellen aan", naam)
print(f"{gender1.capitalize()} leeftijd is:", leeftijd)
print(f"{naam}'s favoriete kleur is:", kleur)
print(f"Het verschil tussen {gender1} leeftijd en {getal} is:", leeftijdn)
