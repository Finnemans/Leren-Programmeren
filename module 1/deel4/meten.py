def gelijk(nr1: int, nr2: int):
    if nr1 == nr2:
        return f'{nr1} en {nr2} zijn even groot'

def groot(nr1: int, nr2: int):
    if nr1 > nr2:
        return f'Maximum: {nr1} en minimum: {nr2}'
    
def klein(nr1: int, nr2: int):
    if nr1 < nr2:
        return f'Maximum: {nr2} en minimum: {nr1}'
