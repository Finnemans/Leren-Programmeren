vara = int(input('vul hier getal A in: '))
varb = int(input('vul hier getal B in: '))

if vara > varb:
    max = vara
    min = varb
    print(f'a is het grootste getal:{max}')
elif vara < varb:
    min = vara
    max = varb
    print(f'a is het kleinste getal:{min}')
else:
    print('a en b zijn even groot')



print(f'het minimum is:{min}')
print(f'het maximum is:{max}')