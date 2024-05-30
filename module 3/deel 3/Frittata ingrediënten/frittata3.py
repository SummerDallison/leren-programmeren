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

milk_ml = unit2ml(amount_milk, UNIT_MILK)
oil_ml = unit2ml(amount_oil, UNIT_OIL)
salt_g = ml2gram(unit2ml(amount_salt, UNIT_SALT), GRAM_PER_ML_SALT)
pepper_g = ml2gram(unit2ml(amount_pepper, UNIT_PEPPER), GRAM_PER_ML_PEPPER)
spinach_g = ml2gram(unit2ml(amount_spinach, UNIT_SPINACH), GRAM_PER_ML_SPINACH)
cheese_g = ml2gram(unit2ml(amount_cheese, UNIT_CHEESE), GRAM_PER_ML_CHEESE)

# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} {str_single_plural(nr_persons, TXT_PERSONS)}:')
print('-----------------------------------------------')
print(f'* {amount_eggs} {str_single_plural(amount_eggs, TXT_EGGS)}')
print(f'* {str_amount_fraction(amount_milk)} {str_units(amount_milk, UNIT_CUPS)} {TXT_MILK} ({format_amount(milk_ml)} ml)')
print(f'* {str_amount_fraction(amount_salt)} {str_units(amount_salt, UNIT_TEASPOONS)} {TXT_SALT} ({format_amount(salt_g)} gram)')
print(f'* {str_amount_fraction(amount_pepper)} {str_units(amount_pepper, UNIT_TEASPOONS)} {TXT_PEPPER} ({format_amount(pepper_g)} gram)')
print(f'* {str_amount_fraction(amount_oil)} {str_units(amount_oil, UNIT_SPOONS)} {TXT_OIL} ({format_amount(oil_ml)} ml)')
print(f'* {amount_onions} {str_single_plural(amount_onions, TXT_ONIONS)}')
print(f'* {amount_garlics} {str_single_plural(amount_garlics, TXT_GARLICS)}')
print(f'* {amount_paprikas} {str_single_plural(amount_paprikas, TXT_PAPRIKAS)}')
print(f'* {str_amount_fraction(amount_spinach)} {str_units(amount_spinach, UNIT_CUPS)} {TXT_SPINACH} ({format_amount(spinach_g)} gram)')
print(f'* {str_amount_fraction(amount_cheese)} {str_units(amount_cheese, UNIT_CUPS)} {TXT_CHEESE} ({format_amount(cheese_g)} gram)')
print('-----------------------------------------------')