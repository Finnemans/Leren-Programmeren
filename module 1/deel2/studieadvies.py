from studieadviestext import*

print(STUDIEDOKTER_TITEL)
print('')
print(AANTAL_WEKEN_VRAAG)
weken = int(input(': '))
print(COMPETENTIE_STELLING_1)
print(OPTIES)
stel1 = int(input(': '))
print(COMPETENTIE_STELLING_2)
print(OPTIES)
stel2 = int(input(': '))
print(COMPETENTIE_STELLING_3)
print(OPTIES)
stel3 = int(input(': '))
print(COMPETENTIE_STELLING_4)
print(OPTIES)
stel4 = int(input(': '))
print(COMPETENTIE_STELLING_5)
print(OPTIES)
stel5 = int(input(': '))
if weken >= 10:
   print(COMPETENTIE_STELLING_6)
   print(OPTIES)
   stel6 = int(input(': '))
   print(COMPETENTIE_STELLING_7)
   print(OPTIES)
   stel7 = int(input(': '))
   som = stel1 + stel2 + stel3 + stel4 + stel5 + stel6 + stel7
   gemiddelde = som / 7
else:
   som = stel1 + stel2 + stel3 + stel4 +stel5
   gemiddelde = som / 5

print(' ')
if gemiddelde <= 2:
   print(f'zorgelijk {gemiddelde}')
   print(COMPETENTIE_ADVIES_ZORGELIJK)
elif gemiddelde <= 3:
   print(f'twijfelachtig {gemiddelde}')
   print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
elif gemiddelde >= 4:
   print(f'geruststellend {gemiddelde}')
   print(COMPETENTIE_ADVIES_GERUSTSTELLEND)

# Ik kan bonus opdracht C niet.