from termcolor import colored, cprint, COLORS

deelnemers = int(input('hoeveel mensen gaan mee: '))
minuten = int(input('hoeveel minuten wil je in de vip: '))

vipprijs = minuten / 5 * 0.37
entree = 7.45

vipprijs = vipprijs * deelnemers
entreeprijs = entree * deelnemers
totaal = vipprijs + entreeprijs

print(f'Dit geweldige dagje-uit met {colored(deelnemers, 'yellow')} mensen in de Speelhal met {colored(minuten, 'yellow')} minuten VR kost je maar {colored(totaal, 'yellow')} euro')