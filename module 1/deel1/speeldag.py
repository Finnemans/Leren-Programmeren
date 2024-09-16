from termcolor import colored, cprint, COLORS

deelnemers = int(input('hoeveel mensen gaan mee: '))
minuten = int(input('hoeveel minuten wil je in de vip: '))
kostenpermin = int(float(input('hoeveel kost het per 5 min: ')) * 100)
# print(permin)

vipprijs = minuten / 5 * kostenpermin
entree = int(float(input('hoeveel kost de entree: ')) * 100)
# print(entree)

vipprijs2 = vipprijs * deelnemers
entreeprijs = entree * deelnemers
totaal = vipprijs2 + entreeprijs

print(f'Dit geweldige dagje-uit met {colored(deelnemers, 'yellow')} mensen in de Speelhal met {colored(minuten, 'yellow')} minuten VR kost je maar {colored(int(totaal), 'yellow')} cent')