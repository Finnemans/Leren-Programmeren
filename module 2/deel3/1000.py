start = 51
antwoord = 0
list = [50]


while antwoord <= 1000:
    list.append(start)
    antwoord = sum(list)
    string = ""
    teller = 0
    for x in list:
        string += f'{x}'
        teller += 1
        if teller != len(list): #laatste waarde geen plus printen
            string += " + "
        
    print(f'{len(list)-1}. {string} = {antwoord}')
    start += 1