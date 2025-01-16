import random
import time

totaalrondes = 20
maxgokken = 10
score = 0

for ronden in range(1, totaalrondes + 1):
    randomgetal = random.randint(1, 1000)
    print(f'Ronde {ronden}.')

    for raden in range(1, maxgokken + 1):
        gok = int(input('Raad het getal van 1 tot 1000: '))
    
        if gok == randomgetal:
            print('Gefeliciteerd, je hebt het getal geraden!')
            score += 1
            break
        elif abs(gok - randomgetal) < 20:
            print('Je bent heel warm!')
        elif abs(gok - randomgetal) < 50:
            print('Je bent warm!')
        elif gok == 1001:
            for x in range(10):
                print('+10.000!')
                score += 100000
                time.sleep(0.4)
            break

        if gok < randomgetal:
            print(f'Hoger dan {gok}!')
        elif gok > randomgetal:
            print(f'Lager dan {gok}!')
    else:
        print(f'Helaas, je hebt het getal niet geraden. Het geheime getal was {randomgetal}.')

    print(f'Je score tot nu toe: {score}.')
    if ronden < totaalrondes:
        doorgaan = input('Nog een getal raden? Y/N: ').lower()
        if doorgaan != 'y':
            break

print(f'Het spel is voorbij! Je eindscore is: {score}.')
