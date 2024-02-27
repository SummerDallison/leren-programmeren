from fruitmand import fruitmand

max_length = 0
fruit_met_langste_naam = None

for fruit in fruitmand:
    if len(fruit['name']) > max_length:
        max_length = len(fruit['name'])
        fruit_met_langste_naam = fruit

print(f"De {fruit_met_langste_naam['name']} ({max_length} letters) heeft een {fruit_met_langste_naam['color']} kleur en een gewicht {fruit_met_langste_naam['weight']/1000} kg.")