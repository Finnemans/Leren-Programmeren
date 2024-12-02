while True:
    try:
        getal = int(input('Voer een getal in: '))
        break
    except ValueError:
        print('Voer een heel getal in')

for x in range(10):
    print(f"{x +1} x {getal} = {getal * (x +1)}")
