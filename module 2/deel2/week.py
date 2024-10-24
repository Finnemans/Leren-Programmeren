week = ('Maandag','Dinsdag','Woensdag','Donderdag','Vrijdag','Zaterdag','Zondag')

print('Alle dagen van de week zijn:')
for dag in week:
    print(f'- {dag}')
print(' ')

print(f'De weekend dagen zijn: {week[5]} & {week[6]}.')
print(' ')

print(f'De werkdagen zijn: {week[0]}, {week[1]}, {week[2]}, {week[3]} & {week[4]}.')
print(' ')

print(f'Alle dagen van de week in omgekeerde volgorde zijn: {week[6]} -> {week[5]} -> {week[4]} -> {week[3]} -> {week[2]} -> {week[1]} -> {week[0]}')
print(' ')

print('De werkdagen in omgekeerde volgorde zijn:')
for dag in week[4::-1]:
    print(f'- {dag}')
print(' ')

print(f'De weekend dagen in omgekeerde volgorde zijn: {week[6]} & {week[5]}.')