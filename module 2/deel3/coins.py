# name of student: Finn Stolk
# number of student: 99080585
# purpose of program: wisselgeld
# structure of program: 
coinValues = [500, 200, 100, 50, 20, 10]  # die euros naar centen
munten = []
aantal = []

toPay = int(float(input('Amount to pay: ')) * 100)  # te betalen van euros naar centen
paid = int(float(input('Paid amount: ')) * 100)  # betaalde van euros naar centen
change = paid - toPay  # berekenen wisselgeld

while change > 0 and len(coinValues) > 0:  # herhaal als er nog wisselgeld en nog een muntwaarde is
    coinValue = coinValues.pop(0)  # haalt de muntwaarde uit de list
    nrCoins = change // coinValue  # bepaalt hoeveel van die munten er nodig zijn

    if nrCoins > 0:  # alleen als er 1 munt van die waarde is
        if coinValue >= 100:  # meer dan 100cent
            print(f"Return maximal {nrCoins}x of {coinValue // 100} euros!") # cent weer als euro
            nrCoinsReturned = int(input(f'How many coins of {coinValue // 100} euros did you return? '))
        else:
            print(f'Return maximal {nrCoins} coins of {coinValue} cents!')
            nrCoinsReturned = int(input(f'How many coins of {coinValue} cents did you return? '))
        
        change -= nrCoinsReturned * coinValue  # nieuw overig te betalen
        
        munten.append(coinValue)  # Sla waarde in centen op
        aantal.append(nrCoinsReturned) # sla aantal munten op

if change > 0: # als na de list nog steeds geld over is
    print(f'Change not returned: {change} cents') # hoeveel wisselgeld nog te betalen
else:
    print('Done!') # klaar

for item1, item2 in zip(munten, aantal):
    if item1 >= 100:  # Voor euro's
        print(f'{item2}x {item1 // 100} euro')
    else:  # Voor centen
        print(f'{item2}x {item1} cent')
