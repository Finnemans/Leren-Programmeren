aantallijstjes = int(input("Hoeveel lijstjes wil je zien? "))
lijsten = []

for x in range(1, aantallijstjes + 1):
    lengte_lijst = int(input(f"Hoe lang moet lijst {x} zijn? "))
    lijstje = []
    for i in range(1, lengte_lijst + 1):
        lijstje.append(x * i)
    lijsten.append(lijstje)

print(lijsten)
