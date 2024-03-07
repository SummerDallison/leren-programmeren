def hello_function(getal):
    resultaat = ""
    for i in range(1, getal+1):
        resultaat += f"Hello from function town {i}!\n"
    return resultaat

print(hello_function(3))
print(hello_function(7))