
naam = input('hoe heet de gastheer: ')
gastheer = True
gasten = int(input('hoeveel gasten komen er: '))
drank = True
chips = True

#Een feest moet minimaal gasten of een gastheer hebben.
start_condition_1 = gastheer or gasten
start_condition_2 = gasten or chips or drank
start_condition_3 = chips
start_condition_4 = gasten >= 4
start_condition_5 = gastheer or drank
start_condition_6 = gastheer or gasten or drank
startcondition7 = naam == 'finn'
startcondition8 = gasten <= 20

if start_condition_1 and start_condition_2 and startcondition8 and startcondition7 and start_condition_3 and start_condition_4 and start_condition_5 and start_condition_6:
    print('Start the Party')
else:
    print('No Party')