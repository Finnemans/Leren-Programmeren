# pizza calc Finn Stolk:

(print("Hoeveel small pizza's wilt u?"))
spizza = int(input('? '))
(print("Hoeveel medium pizza's wilt u?"))
mpizza = int(input('? '))
(print("Hoeveel large pizza's wilt u?"))
lpizza = int(input('? '))

smallprijs = 6.50
mediumprijs = 9.30
largeprijs = 11.10

prijs1 = spizza * smallprijs
prijs2 = mpizza * mediumprijs
prijs3 = lpizza * largeprijs
totaal = prijs1 + prijs2 + prijs3



print('************ KASSA BON ************')
if spizza == int():
   print(f"Pizza's small:   {spizza} x  {smallprijs} =  {prijs1}")
if mpizza == int():
   print(f"Pizza's medium:  {mpizza} x  {mediumprijs} =  {prijs2}")
if lpizza == int():
   print(f"Pizza's large:   {lpizza} x {largeprijs} =  {prijs3}")

print('-----------------------------------')
print(f'Te betalen:                  {totaal}')