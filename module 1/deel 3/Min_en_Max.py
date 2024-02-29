a = int(input("Voer een geheel getal (a) in : "))
b = int(input("Voer een geheel getal (b) in : "))

if a > b:
    Max = a
    Min = b
    print(f"a is het grootst getal : {Max}")
elif a < b:
    Min = a
    Max = b
    print(f"a is het kleinst getal : {Min}")
else: 
    Max = a
    Min = b
    print("a en b zijn even groot.")

print(f"Het minimum is : {Min}")
print(f"Het maximum is : {Max}")