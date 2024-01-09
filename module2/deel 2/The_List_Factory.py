num_lists = int(input("Hoeveel lijstjes? "))

all_lists = []

for i in range(1, num_lists + 1):
    length = int(input(f"Hoeveel lijstjes in {i}? "))
    current_list = list(range(i, i * length + 1, i))
    all_lists.append(current_list)

print(all_lists)