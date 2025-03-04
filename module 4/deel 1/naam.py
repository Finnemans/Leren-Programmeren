def vraag_naam_en_leeftijd():
    naam = input("Wat is je naam? ")
    leeftijd = int(input("Wat is je leeftijd? "))
    return {"name": naam, "age": leeftijd}

persoon = vraag_naam_en_leeftijd()

print(f"{persoon['name']} is {persoon['age']} jaar")