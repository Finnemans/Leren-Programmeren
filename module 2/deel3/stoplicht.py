import time

def stoplicht(tijd:int,kleur:str):
    for i in range(tijd):
        print(kleur)
        time.sleep(1)  

while True:
    stoplicht(20, 'rood')
    stoplicht(30, 'groen')
    stoplicht(10, 'oranje')


#     for i in range(20):
#         print('rood')
#         time.sleep(1)

#     for i in range(30):
#         print('groen')
#         time.sleep(1)

#     for i in range(10):
#         print('oranje')
#         time.sleep(1)