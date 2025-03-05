from termcolor import colored
from functie import verzamel_personen, check_volwassen

personen_lijst = verzamel_personen()

for persoon in personen_lijst:
    naam = colored(persoon['name'].capitalize(), "green")
    stad = colored(persoon['city'].capitalize(), "yellow")

    print(f"In {stad} woont {naam}, die {check_volwassen(persoon['age'])} volwassen is.")