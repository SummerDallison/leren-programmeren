from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = input_nr_persons('Ingrediënten voor hoeveel personen?\n') # replace this with better input

# ----- CALCULATIONS ----
# calculate factor 
factor = nr_persons / RECIPE_PERSONS

# calculate amount_eggs
amount_eggs = round_piece(AMOUNT_EGGS * factor)

# calculate amount_milk
amount_milk = round_quarter(AMOUNT_MILK * factor)

# calculate amount_salt
amount_salt = round_quarter(AMOUNT_SALT * factor)

# calculate amount_pepper
amount_pepper = round_quarter(AMOUNT_PEPPER * factor)

# calculate amount_oil
amount_oil = round_quarter(AMOUNT_OIL * factor)

# calculate amount_onions
amount_onions = round_piece(AMOUNT_ONIONS * factor)

# calculate amount_garlics
amount_garlics = round_piece(AMOUNT_GARLICS * factor)

# calculate amount_spinach
amount_spinach = round_quarter(AMOUNT_SPINACH * factor)

# calculate amount_paprikas
amount_paprikas = round_piece(AMOUNT_PAPRIKAS * factor)

# calculate amount_cheese
amount_cheese = round_quarter(AMOUNT_CHEESE * factor)

# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} {TXT_PERSONS}:')
print('-----------------------------------------------')
print(f'* {amount_eggs} {TXT_EGGS}')
print(f'* {amount_milk} {UNIT_CUPS} {TXT_MILK}')
print(f'* {amount_salt} {UNIT_TEASPOONS} {TXT_SALT}')
print(f'* {amount_pepper} {UNIT_TEASPOONS} {TXT_PEPPER}')
print(f'* {amount_oil} {UNIT_SPOONS} {TXT_OIL}')
print(f'* {amount_onions} {TXT_ONIONS}')
print(f'* {amount_garlics} {TXT_GARLICS}')
print(f'* {amount_paprikas} {TXT_PAPRIKAS}')
print(f'* {amount_spinach} {UNIT_CUPS} {TXT_SPINACH}')
print(f'* {amount_cheese} {UNIT_CUPS} {TXT_CHEESE}')
print('-----------------------------------------------')