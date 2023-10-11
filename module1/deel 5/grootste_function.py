from test_lib import test, report

def determine_biggest(nr1: int, nr2: int) -> str:
    if nr1 < nr2:
        antwoord = (f"Maximum: {nr2} and minimum: {nr1}") 
    elif nr1 > nr2:
        antwoord = (f"Maximum: {nr1} and minimum: {nr2}")
    else:
        antwoord = ("Beide getallen zijn even groot")

    return antwoord

nr1 = 10
nr2 = 20
verwacht = (f"Maximum: {nr2} and minimum: {nr1}") 
resultaat = determine_biggest(nr1, nr2)
test("Test 1", verwacht, resultaat)

nr1 = 20
nr2 = 10
verwacht = (f"Maximum: {nr1} and minimum: {nr2}")
resultaat = determine_biggest(nr1, nr2)
test("Test 2", verwacht, resultaat)

nr1 = 10
nr2 = 10
verwacht = "Beide getallen zijn even groot"
resultaat = determine_biggest(nr1, nr2)
test("Test 3", verwacht, resultaat)

report()