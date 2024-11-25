thisdict = {"wolf":"puppy", "tanden":"tandjes", "klauwen":"pootjes", "snel":"traag", "prooi":"knuffel",}

zin = input("Schrijf een verhaaltje over een wolf gebruik de woorden: Wolf, Tanden, Klauwen, Snel, Prooi : ")

# woorden = zin.split()

# woorden2 = [thisdict.get(x, x) for x in woorden]
for key,value in thisdict.items():
    zin = zin.replace(f'{key}',f'{value}')
    zin = zin.replace(f'{key.capitalize()}',f'{value.capitalize()}')


# vertaalde_tekst = " ".join(woorden2)

print(" ")
print(" ")
print(zin) 