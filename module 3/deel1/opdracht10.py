from fruitmand import fruitmand

sorted_fruitmand = sorted(fruitmand, key=lambda x: x['weight'])[::-1]

for fruit in sorted_fruitmand:
    print(fruit['name'])
    print(fruit['weight'])

#heb ik gemaakt met chatgpt  key=lambda x: x['weight']) snap dit niet echt