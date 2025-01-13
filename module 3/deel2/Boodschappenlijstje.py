list= ['bier','wijn','hagelslag','brood','beleg','melk','bananen','chips']
bon = []
bonaantal = []
var1 = True
while var1 == True:
    while True:
        artikel = input('Welk artikel wilt u toevoegen? / geen: ').lower()
        if artikel == 'geen':
            var1 = False
            break
        elif artikel in list:
            var1 = True
            break
        else:
            print(f"Artikel: '{artikel}' wordt niet herkend. Probeer het opnieuw.")

    if var1 == True:
        while True:
            try:
                aantal = int(input(f'Hoeveel {artikel} wilt u toevoegen? '))
                break
            except ValueError:
                print('Voer alstublieft een geheel getal in.')
        if artikel in bon:
            index = bon.index(artikel)
            bonaantal[index] += aantal
        else:
            bon.append(artikel)
            bonaantal.append(aantal)
print('-[ Boodschappenlijst]-')
print('')
for item1, item2 in zip(bonaantal, bon):
    print(f'{item1}x {item2}')
print('')
print(22 * '-')