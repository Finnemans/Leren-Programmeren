# name of student: Finn Stolk
# number of student: 99080585
# purpose of program: wisselgeld
# structure of program: 
coinValues = [1000, 500, 200, 100, 50, 20, 10]  # die euros naar centen

toPay = int(float(input('Amount to pay: ')) * 100)  #
paid = int(float(input('Paid amount: ')) * 100)  #
change = paid - toPay  #

while change > 0 and len(coinValues) > 0:  
    coinValue = coinValues.pop(0)  #
    nrCoins = change // coinValue  #

    if nrCoins > 0:  #
        if coinValue >= 100:  # meer dan 100cent
            print(f"Return maximal {nrCoins}x of {coinValue // 100} euros!") # cent weer als euro
            nrCoinsReturned = int(input(f'How many times of {coinValue // 100} euros did you return? '))
        else:
            print(f'Return maximal {nrCoins} coins of {coinValue} cents!')
            nrCoinsReturned = int(input(f'How many coins of {coinValue} cents did you return? '))
        
        change -= nrCoinsReturned * coinValue  # nieuw overig te betalen

if change > 0:
    print(f'Change not returned: {change} cents')
else:
    print('Done!')