week = ('Maandag','Dinsdag','Woensdag','Donderdag','Vrijdag','Zaterdag','Zondag')

print('Alle dagen van de week zijn:')
for dag in week:
    print(f'- {dag}')
print(' ')

print(f'De weekend dagen zijn:')
for dag in week[-2:]:
    print(f'- {dag}')
print(' ')

print(f'De werkdagen zijn:')
for dag in week[:5]:
    print(f'- {dag}')
print(' ')

print(f'Alle dagen van de week in omgekeerde volgorde zijn:')
for dag in week[::-1]:
   print(f'- {dag}')

print('De werkdagen in omgekeerde volgorde zijn:')
for dag in week[4::-1]:
    print(f'- {dag}')
print(' ')

print(f'De weekend dagen in omgekeerde volgorde zijn:')
for dag in week[-1:-3:-1]:
    print(f'- {dag}')