# pizza calc Finn Stolk:

smallprijs = 6.50
mediumprijs = 9.30
largeprijs = 11.10
totaal = 0

try:
   (print("Hoeveel small pizza's wilt u?"))
   pizza = int(input('? '))
   bedrag = pizza * smallprijs
   totaal += bedrag
   text1 = f"Pizza's small:   {pizza} x  {smallprijs:.2f} =  {bedrag}"
except: 
   print('Dit is geen heel nummer!')
   text1 = ''

try:
   (print("Hoeveel medium pizza's wilt u?"))
   pizza = int(input('? '))
   bedrag = pizza * mediumprijs
   totaal += bedrag
   text2 = f"Pizza's medium:  {pizza} x  {mediumprijs} =  {bedrag}"
except:
   print('Dit is geen heel nummer!')
   text2 = ''

try:
   (print("Hoeveel large pizza's wilt u?"))
   pizza = int(input('? '))
   bedrag = pizza * largeprijs
   totaal += bedrag
   text3 = f"Pizza's large:   {pizza} x {largeprijs} =  {bedrag}"
except:
    print('Dit is geen heel nummer!')
    text3 = ''

print('************ KASSA BON ************')
print(text1)
print(text2)
print(text3)
print('-----------------------------------')
print(f'Te betalen:                  {totaal}')