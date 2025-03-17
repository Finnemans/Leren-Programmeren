import lambdaa
first_round = True
n1 = None

while True:
    try:
        if first_round:
            print("Wat wilt u doen?")
            print("A) optellen")
            print("B) aftrekken")
            print("C) vermenigvuldigen")
            print("D) delen")
            print("E) ophogen")
            print("F) verlagen")
            print("G) verdubbelen")
            print("H) halveren")
            keuze = input('Kies: ').upper()
            n1 = float(input("Voer het eerste getal in: "))
        else:
            print(f"Wat wilt u doen met de uitkomst ({n1})?")
            print("A) optellen")
            print("B) aftrekken")
            print("C) vermenigvuldigen")
            print("D) delen")
            print("E) ophogen")
            print("F) verlagen")
            print("G) verdubbelen")
            print("H) halveren")
            print("I) niets")
            keuze = input('Kies: ').upper()
            if keuze == "I":
                print("Einde berekening.")
                break

        if keuze in ["A", "B", "C", "D"]:
            n2 = float(input(f"Wat wilt u bij {n1} {'optellen' if keuze == 'A' else 'aftrekken' if keuze == 'B' else 'vermenigvuldigen' if keuze == 'C' else 'delen'}? "))
        elif keuze in ["E", "F"]:
            n2 = 1
        elif keuze in ["G", "H"]:
            n2 = 2
        else:
            print("Ongeldige keuze. Probeer opnieuw.")
            continue

        if keuze == "A":
            result = lambdaa.calculations["add"](n1, n2)
            print(f"{n1} + {n2} = {result}")
        elif keuze == "B":
            result = lambdaa.calculations["subtract"](n1, n2)
            print(f"{n1} - {n2} = {result}")
        elif keuze == "C":
            result = lambdaa.calculations["multiply"](n1, n2)
            print(f"{n1} x {n2} = {result}")
        elif keuze == "D":
            result = lambdaa.calculations["divide"](n1, n2)
            if isinstance(result, str):
                print(result)
                continue
            print(f"{n1} : {n2} = {result}")
        elif keuze == "E":
            result = lambdaa.calculations["add"](n1, n2)
            print(f"{n1} + 1 = {result}")
        elif keuze == "F":
            result = lambdaa.calculations["subtract"](n1, n2)
            print(f"{n1} - 1 = {result}")
        elif keuze == "G":
            result = lambdaa.calculations["multiply"](n1, n2)
            print(f"{n1} x 2 = {result}")
        elif keuze == "H":
            result = lambdaa.calculations["divide"](n1, n2)
            if isinstance(result, str):
                print(result)
                continue
            print(f"{n1} : 2 = {result}")

        n1 = result
        first_round = False

    except ValueError:
        print("Ongeldige invoer, probeer opnieuw.")
