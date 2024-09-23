import random

num1 = random.randint(1,10)
num2 = random.randint(5,15)

try:
    number = int(input(f'Weet jij wat {num1} + {num2} is? '))
    if number == (num1 + num2):
        print('Dat is juist')
    elif number != (num1 + num2):
        print('Nee dat klopt niet')
except:
        print('Dat is geen nummer!')
