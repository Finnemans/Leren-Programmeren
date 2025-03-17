calculations = {
    "optellen": lambda getal1, getal2: f"{getal1} + {getal2} = {getal1 + getal2}",
    "aftrekken": lambda getal1, getal2: f"{getal1} - {getal2} = {getal1 - getal2}",
    "vermenigvuldigen": lambda getal1, getal2: f"{getal1} * {getal2} = {getal1 * getal2}",
    "delen": lambda getal1, getal2: f"{getal1} / {getal2} = {'Error: Kan niet delen door nul' if getal2 == 0 else getal1 / getal2}"
}

print(calculations["optellen"](10, 5))
print(calculations["aftrekken"](10, 5))
print(calculations["vermenigvuldigen"](10, 5))
print(calculations["delen"](10, 5))