import random

mm_colors = ['rood','blauw','groen','geel','bruin']

while True:
    try:
        num_mms_to_add = int(input("Hoeveel M&M's moeten er aan de zak worden toegevoegd worden? "))
        break
    except ValueError:
        print("Voer alstublieft een getal in.")

mm_bag = {}

for i in range(num_mms_to_add):
    random_color = random.choice(mm_colors)
    if random_color in mm_bag:
        mm_bag[random_color] += 1
    else:
        mm_bag[random_color] = 1

print(f"Inhoud van de M&M-zak: {mm_bag}")