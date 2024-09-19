def convertToEuroText (amount):
    return "€{:.2f}".format(float(amount)).replace(".", ",")

SMALL_PRICE = 1.25
MEDIUM_PRICE = 2.10

amount1 = float(input(f'Hoeveel ijsjes van {SMALL_PRICE} wil je bestellen? '.format(convertToEuroText(SMALL_PRICE))))
amount2 = float(input(f'En hoeveel ijsjes van {MEDIUM_PRICE} wil je bestellen? '.format(convertToEuroText(MEDIUM_PRICE))))
totalPrice = float(amount1 * SMALL_PRICE) + float(amount2 * MEDIUM_PRICE)

print(f'Dat is dan {totalPrice} totaal')