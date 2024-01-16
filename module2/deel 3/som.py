total = 0
num = 50
iteratie = 1

while total <= 1000:
    total += num 
    print(f"{iteratie}. { ' + '.join(map(str, range(50, num + 2)))} = {total}")
    iteratie += 1
    num += 1