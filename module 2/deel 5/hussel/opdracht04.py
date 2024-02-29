from fruitmand import fruitmand
import random

amount = int(input("Voer een aantal in: "))

fruit_count = {}

for i in range(amount):
    random_fruit = random.choice(fruitmand)
    fruit_name = (random_fruit["name"])
    fruit_count[fruit_name] = fruit_count.get(fruit_name, 0) + 1

for fruit, aantal in fruit_count.items():
    print(f"{aantal}x {fruit}")