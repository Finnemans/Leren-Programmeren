from functies import *
from data import *

runnen = True

while runnen:
    klant_type = kiesKlantType()

    # PARTICULIERE KLANT
    if klant_type == 1:
        totaal_bolletjes = 0
        aantal_hoorntjes = 0
        aantal_bakjes = 0
        smaken_totaal = []
        toppings_totaal = []

        bestellen = True
        while bestellen:
            bolletjes = aantalBolletjes()
            totaal_bolletjes += bolletjes

            # if bolletjes <= 3:
            verpakking = soortBakken(bolletjes)
            # else:
            #     verpakking = 'bakje'

            if verpakking == 'hoorntje':
                aantal_hoorntjes += 1
            else:
                aantal_bakjes += 1

            smaken = smakenKiezen(bolletjes)
            smaken_totaal.extend(smaken)

            toppings = toppingsKiezen()
            toppings_totaal.extend(toppings)

            print(f"Hier is uw {verpakking} met {bolletjes} bolletje(s).")

            if not nogMeerBestellen():
                bestellen = False

        print('-------- ["Papi Gelato"] --------')
        totaal_prijs = 0

        for smaak in ['aardbei', 'chocolade', 'munt', 'vanille']:
            aantal = smaken_totaal.count(smaak)
            if aantal > 0:
                prijs = aantal * PRIJS_BOLLETJE
                totaal_prijs += prijs
                print(f"{smaak.capitalize():10} {aantal} x €{PRIJS_BOLLETJE:.2f} = €{prijs:.2f}")

        if aantal_hoorntjes > 0:
            prijs = aantal_hoorntjes * PRIJS_HOORNTJE
            totaal_prijs += prijs
            print(f"Hoorntjes  {aantal_hoorntjes} x €{PRIJS_HOORNTJE:.2f} = €{prijs:.2f}")

        if aantal_bakjes > 0:
            prijs = aantal_bakjes * PRIJS_BAKJE
            totaal_prijs += prijs
            print(f"Bakjes     {aantal_bakjes} x €{PRIJS_BAKJE:.2f} = €{prijs:.2f}")

        toppings_prijs = 0
        for topping in toppings_totaal:
            if topping == 'slagroom':
                toppings_prijs += SLAGROOM
            elif topping == 'sprinkels':
                toppings_prijs += SPRINKELS
            elif topping == 'caramel saus':
                toppings_prijs += CARAMEL_SAUS

        if toppings_prijs > 0:
            totaal_prijs += toppings_prijs
            print(f"Toppings             = €{toppings_prijs:.2f}")

        print("--------------------------")
        print(f"Totaal te betalen: €{totaal_prijs:.2f}")
        print("Bedankt en tot ziens!")

    # ZAKELIJKE KLANT
    else:
        smaken_liters = litersBestellen()

        print('-------- ["Papi Gelato"] --------')
        totaal = 0

        for smaak in ['aardbei', 'chocolade', 'munt', 'vanille']:
            aantal = smaken_liters.count(smaak)
            if aantal > 0:
                if smaak == 'aardbei':
                    prijs = aantal * LITER_AARDBEI
                elif smaak == 'chocolade':
                    prijs = aantal * LITER_CHOCOLADE
                elif smaak == 'munt':
                    prijs = aantal * LITER_MUNT
                else:
                    prijs = aantal * LITER_VANILLE

                totaal += prijs
                print(f"{smaak.capitalize():10} {aantal} x €{prijs/aantal:.2f} = €{prijs:.2f}")

        btw = totaal * BTW_PERCENTAGE

        print("--------------------------")
        print(f"Totaal excl. BTW: €{totaal - btw:.2f}")
        print(f"BTW ({int(BTW_PERCENTAGE*100)}%):        €{btw:.2f}")
        print(f"Totaal incl. BTW: €{totaal:.2f}")
        print("Bedankt en tot ziens!")

    doorgaan = input("Druk op S om te stoppen of Enter om opnieuw te starten...").lower()
    klant_type == 0
    if doorgaan == 's':
        runnen = False
