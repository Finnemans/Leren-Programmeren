
gastheer = False
gasten = False
drank = False
chips = True

#Een feest moet minimaal gasten of een gastheer hebben.
start_condition_1 = gastheer or gasten
start_condition_2 = gasten or chips or drank
start_condition_3 = chips
start_condition_4 = gasten
start_condition_5 = gastheer or drank
start_condition_6 = gastheer or gasten or drank

if start_condition_1 and start_condition_2 and start_condition_3 and start_condition_4 and start_condition_5 and start_condition_6:
    print('Start the Party')
else:
    print('No Party')

