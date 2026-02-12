# pizza calc Finn Stolk:

smallprijs = 6.50
mediumprijs = 9.30
largeprijs = 11.10
totaal = 0
text = ""

def ask(prompt, prijs, size):
   global totaal, text
   try:
      (print(prompt))
      pizza = int(input('? '))
      bedrag = pizza * prijs
      totaal += bedrag
      text += f"Pizza's {size}:   {pizza} x  {prijs:.2f} =  {bedrag}\n"
   except: 
      print('Dit is geen heel nummer!')
      text1 += ''

ask("Hoeveel small pizza's wilt u?", smallprijs, 'small')
ask("Hoeveel medium pizza's wilt u?", mediumprijs, 'medium')
ask("Hoeveel large pizza's wilt u?", largeprijs, 'large')

text = text.strip()

print('************ KASSA BON ************')
print(text)
print('-----------------------------------')
print(f'Te betalen:                  {totaal}')