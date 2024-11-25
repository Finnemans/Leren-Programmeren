start = 50
antwoord = 0
list = [ ]

while antwoord <= 1000:
    list.append(start)
    antwoord = sum(list)
    print(f"{len(list)}. {list} = {antwoord}")
    start += 1