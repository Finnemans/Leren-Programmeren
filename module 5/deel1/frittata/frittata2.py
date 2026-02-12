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

print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} {str_single_plural(nr_persons, TXT_PERSONS)}:')
print('-----------------------------------------------')
print(f"{eggs} {str_single_plural(eggs, TXT_EGGS)}")
print(f"{str_amount_fraction(milk)} {str_units(milk, UNIT_CUPS)} {TXT_MILK}")
print(f"{str_amount_fraction(salt)} {str_units(salt, UNIT_TEASPOONS)} {TXT_SALT}")
print(f"{str_amount_fraction(pepper)} {str_units(pepper, UNIT_TEASPOONS)} {TXT_PEPPER}")
print(f"{str_amount_fraction(oil)} {str_units(oil, UNIT_SPOONS)} {TXT_OIL}")
print(f"{onions} {str_single_plural(onions, TXT_ONIONS)}")
print(f"{garlics} {str_single_plural(garlics, TXT_GARLICS)}")
print(f"{paprikas} {str_single_plural(paprikas, TXT_PAPRIKAS)}")
print(f"{str_amount_fraction(spinach)} {str_units(spinach, UNIT_CUPS)} {TXT_SPINACH}")
print(f"{str_amount_fraction(cheese)} {str_units(cheese, UNIT_CUPS)} {TXT_CHEESE}")
print('-----------------------------------------------')