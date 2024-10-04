from meten import gelijk, groot, klein
from test_lib import test, report

nr1 = int(input('Vul hier getal A in: '))
nr2 = int(input('Vul hier getal B in: '))

expected = f'{nr1} en {nr2} zijn even groot' #resultaat
result = gelijk(nr1, nr2) #roep hier je functie aan met 2 dezelfde getallen
test('TEST nr1=nr2', expected, result)

expected = f'Maximum: {nr1} en minimum: {nr2}'#resultaat
result = groot(nr1, nr2)
test('TEST nr1>nr2', expected, result)

expected = f'Maximum: {nr2} en minimum: {nr1}' #resultaat
result = klein(nr1, nr2) #roep hier je functie aan  waar nr1 kleiner is dan nr2
test('TEST nr1<nr2', expected, result)

if __name__ == "__main__":
    report()