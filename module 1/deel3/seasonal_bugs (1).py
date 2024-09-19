print('Welk seizoen vind jij het fijnst?', 
      "A) Lente", 
      "B) Zomer", 
      "C) Herfst", 
      "D) Winter")
gekozen_seizoen = input('? ')

if (gekozen_seizoen == 'a' or gekozen_seizoen =='c'):
    print('Dus jij vindt een tussenseizoen het fijnst...')
    weer_type = ''
elif (gekozen_seizoen == 'b'):
    weer_type = 'warm'
else:
    weer_type = 'koud'

if len(weer_type) > 0:
    print(f'Dus jij houd van {weer_type} weer!')