deelnemers = 4
entree = 7.45
vip = 0.37
viptijd = 9

vipprijs = vip * viptijd * deelnemers
entreeprijs = entree * deelnemers
totaal = vipprijs + entreeprijs

print(f'Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar {totaal} euro')