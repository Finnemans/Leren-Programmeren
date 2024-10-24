from meten import gelijk, groot, klein
from test_lib import test, report

# nr1 = int(input('Vul hier getal A in: '))
# nr2 = int(input('Vul hier getal B in: '))

expected = f'{5} en {5} zijn even groot' #resultaat
result = gelijk(5, 5) #roep hier je functie aan met 2 dezelfde getallen
test('TEST nr1=nr2', expected, result)

expected = f'Maximum: {10} en minimum: {4}'#resultaat
result = groot(10, 4)
test('TEST nr1>nr2', expected, result)

expected = f'Maximum: 7 en minimum: 3' #resultaat
result = klein(3, 7) #roep hier je functie aan  waar nr1 kleiner is dan nr2
test('TEST nr1<nr2', expected, result)

if __name__ == "__main__":
    report()