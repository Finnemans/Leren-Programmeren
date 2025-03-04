def hello_function(nummer):
    for x in range(1, nummer + 1):
        print(f"Hello from function town {x}!")

getal = int(input('Vul een getal in: '))
hello_function(getal)