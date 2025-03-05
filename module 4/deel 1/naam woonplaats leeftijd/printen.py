from functie import verzamel_personen

personen_lijst = verzamel_personen()

for persoon in personen_lijst:
    print(f"{persoon['name']}, die in {persoon['city']} woont, is {persoon['age']} jaar")
