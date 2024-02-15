from fruitmand import fruitmand

for fruit in fruitmand:
    if not fruit["round"]:
        print(fruit["name"])