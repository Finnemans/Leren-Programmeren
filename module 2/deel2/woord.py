thisdict = {"wolf":"puppy", "tanden":"tandjes", "klauwen":"pootjes", "snel":"sloom", "prooi":"knuffel",}

zin = input("Schrijf een verhaaltje over een wolf gebruik de woorden: Wolf, Tanden, Klauwen, Snel, Prooi : ")

woorden = zin.split()

woorden2 = [thisdict.get(woord, woord) for woord in woorden]

vertaalde_tekst = " ".join(woorden2)

print(" ")
print(" ")
print(vertaalde_tekst)
