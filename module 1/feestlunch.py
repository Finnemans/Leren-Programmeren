from termcolor import colored, cprint, COLORS

croissantjes = 17
stokbroden = 2
bonnen = 3

var1 = croissantjes * 0.39
var2 = stokbroden * 2.
var3 = bonnen * 0.50

antwoord = var1 + var2 - var3

print(f"De feestlunch kost je bij de bakker {colored(antwoord, 'yellow', attrs=['bold'])} euro voor de {colored(croissantjes, 'yellow', attrs=['bold'])} croissantjes en de {colored(stokbroden, 'yellow', attrs=['bold'])} stokbroden als de {colored(bonnen, 'yellow', attrs=['bold'])} kortingsbonnen nog geldig zijn!")