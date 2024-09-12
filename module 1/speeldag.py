from termcolor import colored, cprint, COLORS

deelnemers = 4
entree = 7.45
vip = 0.37
viptijd = 9

minuten = viptijd * 5
vipprijs = vip * viptijd * deelnemers
entreeprijs = entree * deelnemers
totaal = vipprijs + entreeprijs

print(f'Dit geweldige dagje-uit met {colored(deelnemers, 'yellow')} mensen in de Speelhal met {colored(minuten, 'yellow')} minuten VR kost je maar {colored(totaal, 'yellow')} euro')