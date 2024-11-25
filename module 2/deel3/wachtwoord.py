pogingen = 0
over = 5

ww = input('maak een wachtwoord aan: ')

while over > 0:
    check = input('Vul je wachtwoord in: ')
    
    if check == ww:
        print('Correct')
        pogingen += 1
        print(f'Je hebt het na {pogingen} poging(en) goed.')
        break
    else:
        over -= 1
        pogingen += 1
        print('Dat is niet correct, Probeer het opnieuw.')
        print(f'Je hebt nog {over} poging(en) over.')
        if over == 0:
            print('Je hebt geen pogingen meer over. Je mag niet inloggen')