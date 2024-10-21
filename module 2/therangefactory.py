aantal_lijstjes = int(input("Hoeveel lijstjes wil je tonen? "))
lijstjes = []

for x in range(1, aantal_lijstjes + 1):
    lengte_lijstje = int(input(f"Wat is de lengte van lijstje {x}? "))
    lijst = [x * stap for stap in range(1, lengte_lijstje + 1)]
    lijstjes.append(lijst)
print(lijstjes)
