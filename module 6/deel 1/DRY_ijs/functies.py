from data import *


def kiesKlantType() -> int:
    while True:
        keuze = input(
            "Bent u 1) een particuliere klant of 2) een zakelijke klant?: "
        )
        if keuze == '1':
            return 1
        elif keuze == '2':
            return 2
        else:
            print("Sorry dat snap ik niet...")


def aantalBolletjes():
    while True:
        try:
            bolletjes = int(input(f"Hoeveel bolletjes wilt u? ({MIN_BOLLETJES}-{MAX_BOLLETJES}): "))

            if bolletjes > MAX_BOLLETJES:
                print("Sorry, zulke grote bakken hebben wij niet.")
            elif bolletjes < MIN_BOLLETJES:
                print("Sorry dat snap ik niet...")
            else:
                return bolletjes

        except ValueError:
            print("Sorry dat snap ik niet...")


def smakenKiezen(bolletjes: int) -> list:
    smaken = []

    for i in range(bolletjes):
        while True:
            smaak = input(
                f"Welke smaak wilt u voor bolletje nummer {i + 1}? "
                "A) Aardbei, C) Chocolade, M) Munt of V) Vanille?: "
            ).lower()

            if smaak == 'a':
                smaken.append('aardbei')
                break
            elif smaak == 'c':
                smaken.append('chocolade')
                break
            elif smaak == 'm':
                smaken.append('munt')
                break
            elif smaak == 'v':
                smaken.append('vanille')
                break
            else:
                print("Sorry dat snap ik niet...")

    return smaken


def toppingsKiezen() -> list:
    while True:
        topping = input(
            "Welke topping wilt u? "
            "A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?: "
        ).lower()

        if topping == 'a':
            return []
        elif topping == 'b':
            return ['slagroom']
        elif topping == 'c':
            return ['sprinkels']
        elif topping == 'd':
            return ['caramel saus']
        else:
            print("Sorry dat snap ik niet...")


def soortBakken(bolletjes: int) -> str:
    while True:
        if bolletjes <= 3:
            typebakje = input(f"Wilt u deze {bolletjes} bolletje(s) in een hoorntje of een bakje?: ").lower()

            if typebakje in ('hoorntje', 'h'):
                return 'hoorntje'
            elif typebakje in ('bakje', 'b'):
                return 'bakje'
            else:
                print("Sorry dat snap ik niet...")
        else:
            return 'bakje'


def nogMeerBestellen() -> bool:
    while True:
        antwoord = input("Wilt u nog meer bestellen? (j/n): ").lower()

        if antwoord in ('ja', 'j'):
            return True
        elif antwoord in ('nee', 'n'):
            return False
        else:
            print("Sorry, dat snap ik niet...")


def litersBestellen() -> list:
    smaken = []
    while True:
        try:
            liters = int(input("Hoeveel liter ijs wilt u bestellen?: "))
            if liters <= 0:
                print("Sorry dat snap ik niet...")
                continue

            for i in range(liters):
                while True:
                    smaak = input(
                        f"Welke smaak wilt u voor liter nummer {i + 1}? "
                        "A) Aardbei, C) Chocolade, M) Munt of V) Vanille?: "
                    ).lower()

                    if smaak == 'a':
                        smaken.append('aardbei')
                        break
                    elif smaak == 'c':
                        smaken.append('chocolade')
                        break
                    elif smaak == 'm':
                        smaken.append('munt')
                        break
                    elif smaak == 'v':
                        smaken.append('vanille')
                        break
                    else:
                        print("Sorry dat snap ik niet...")
            return smaken

        except ValueError:
            print("Sorry dat snap ik niet...")