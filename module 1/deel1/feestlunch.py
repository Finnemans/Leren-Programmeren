from termcolor import colored, cprint, COLORS

croissantjes = int(input('hoeveel croissantjes wil je: '))
prijscroissantjes = int(float(input('prijs per croissantje: ')) * 100)

stokbroden = int(input('hoeveel stokbroden wil je: '))
prijsstokbroden = int(float(input('prijs per stokbrood: ')) * 100)

bonnen = int(input('hoeveel bonnen heb je: '))
prijsbonnen = int(float(input('hoeveel waarden hebben de bonnen: ')) * 100)

var1 = croissantjes * prijscroissantjes
var2 = stokbroden * prijsstokbroden
var3 = bonnen * prijsbonnen

antwoord = var1 + var2 - var3

print(f"De feestlunch kost je bij de bakker {colored(antwoord, 'yellow', attrs=['bold'])} euro voor de {colored(croissantjes, 'yellow', attrs=['bold'])} croissantjes en de {colored(stokbroden, 'yellow', attrs=['bold'])} stokbroden als de {colored(bonnen, 'yellow', attrs=['bold'])} kortingsbonnen nog geldig zijn!")