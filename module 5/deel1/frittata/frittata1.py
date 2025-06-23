from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = input_nr_persons("Hoeveel mensen eten mee?: ") # replace this with better input

# ----- CALCULATIONS ----
# calculate factor 
factor = nr_persons / 4

# calculate amount_eggs
eggs = round_piece(AMOUNT_EGGS * factor)
# calculate amount_milk
milk = round_quarter(AMOUNT_MILK * factor)
# calculate amount_salt
salt = round_quarter(AMOUNT_SALT * factor)
# calculate amount_pepper
pepper = round_quarter(AMOUNT_PEPPER * factor)
# calculate amount_oil
oil = round_quarter(AMOUNT_OIL * factor)
# calculate amount_onions
onions = round_piece(AMOUNT_ONIONS * factor)
# calculate amount_garlics
garlics = round_piece(AMOUNT_GARLICS * factor)
# calculate amount_spinach
spinach = round_quarter(AMOUNT_SPINACH * factor)
# calculate amount_paprikas
paprikas = round_piece(AMOUNT_PAPRIKAS * factor)
# calculate amount_cheese
cheese = round_quarter(AMOUNT_CHEESE * factor)
# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')
# print (formatted) all amounts and units combined with their ingrediënt descriptions
print(f"{eggs} {TXT_EGGS}")
print(f"{milk} {TXT_MILK}")
print(f"{salt} {TXT_SALT}")
print(f"{pepper} {TXT_PEPPER}")
print(f"{oil} {TXT_OIL}")
print(f"{onions} {TXT_ONIONS}")
print(f"{garlics} {TXT_GARLICS}")
print(f"{paprikas} {TXT_PAPRIKAS}")
print(f"{spinach} {TXT_SPINACH}")
print(f"{cheese} {TXT_CHEESE}")
print('-----------------------------------------------')