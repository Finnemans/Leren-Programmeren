# pizza calc Finn Stolk:

smallprijs = 6.50
mediumprijs = 9.30
largeprijs = 11.10
totaal = 0

try:
   (print("Hoeveel small pizza's wilt u?"))
   spizza = int(input('? '))
   prijs1 = spizza * smallprijs
   totaal += prijs1
   text1 = f"Pizza's small:   {spizza} x  {smallprijs} =  {prijs1}"
except: 
   print('Dit is geen heel nummer!')
   text1 = ''

try:
   (print("Hoeveel medium pizza's wilt u?"))
   mpizza = int(input('? '))
   prijs2 = mpizza * mediumprijs
   totaal += prijs2
   text2 = f"Pizza's medium:  {mpizza} x  {mediumprijs} =  {prijs2}"
except:
   print('Dit is geen heel nummer!')
   text2 = ''

try:
   (print("Hoeveel large pizza's wilt u?"))
   lpizza = int(input('? '))
   prijs3 = lpizza * largeprijs
   totaal += prijs3
   text3 = f"Pizza's large:   {lpizza} x {largeprijs} =  {prijs3}"
except:
    print('Dit is geen heel nummer!')
    text3 = ''

print('************ KASSA BON ************')
print(text1)
print(text2)
print(text3)
print('-----------------------------------')
print(f'Te betalen:                  {totaal}')