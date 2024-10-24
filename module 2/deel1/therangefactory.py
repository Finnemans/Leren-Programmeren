aantallijstjes = int(input("Hoeveel lijstjes wil je zien? "))
lijsten = []

for x in range(aantallijstjes):
    lengte_lijst = int(input(f"Hoe lang moet lijst {x +1} zijn? "))
    lijstje = []
    for i in range(1, lengte_lijst + 1):
        lijstje.append((x+1) * i)
    lijsten.append(lijstje)

print(lijsten)
