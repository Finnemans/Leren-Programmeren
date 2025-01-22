VIP_LIST = ('jeroen', 'jouke', 'rudi')
while True:
    try:
        leeftijd = int(input('Hoe oud ben je? '))
        break
    except ValueError:
        print('Voer alstublieft een geheel getal in.')
while True:
    if leeftijd < 18:
        print('Sorry je mag niet naar binnen.')
        over = 18 - leeftijd
        print(f'Probeer het in {over} jaar nog eens.')
        exit()
    else:
        naam = input('Wat is je naam? ')
        naam = naam.lower()
        if naam in VIP_LIST:
            vip = True
        else:
            vip = False

    if vip == True:
        if leeftijd >= 21:
            bandje = 'blauw'
        else:
            bandje = 'rood'
        print(f'Je krijgt van mij een {bandje} bandje.')
    elif vip == False:
        bandje = False
        if leeftijd >= 21:
            print('Je krijgt van mij een stempel.')
            stempel = True

    while True:
        dorst = input('Wil je wat drinken? Y/N: ')
        dorst.lower()
        if dorst == 'y':
            break
        elif dorst == 'n':
            exit()
        else:
            print('Ongeldig antwoord.')
    
    if dorst == 'y':
        while True:
            drinken = input('wat wil je drinken? ')
            drinken.lower()
            if drinken == 'cola':
                prijs = 1.80
                break
            elif drinken == 'bier':
                prijs = 2.40
                break
            elif drinken == 'champagne':
                prijs = 12.30
                break
            else:
                print('Sorry geen idee wat je bedoeld, hier is een glaasje water')
                exit()

    if vip == False and drinken != 'champagne':
        print(f'Alsjeblieft je {drinken}, dat is dan €{prijs:.2f} Euro')
    elif vip == True and drinken != 'champagne':
        print('Alstublieft, complimenten van het huis.')
    elif vip == False and drinken == 'champagne':
        print('Sorry alleen vips mogen champagne bestellen.')
        exit()
    else:
        if drinken == 'champagne':
            if vip == True:
                if bandje == 'rood':
                    print('sorry je mag geen alcohol bestellen onder de 21')
                    over = 21 - leeftijd
                    print(f'Probeer het in {over} jaar nog eens.')
                    exit()
                elif bandje == 'blauw':
                    print(f'Alsjeblieft je {drinken}, dat is dan €{prijs:.2f} Euro')
    exit()