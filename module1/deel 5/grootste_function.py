def determine_biggest(nr1: int, nr2: int) -> str:
    if nr1 < nr2:
        print(f"Maximum: {nr2} and minimum: {nr1}")
        return str(f"Maximum: {nr2} and minimum: {nr1}") 
    elif nr1 > nr2:
        print(f"Maximum: {nr1} and minimum: {nr2}")
        return str(f"Maximum: {nr1} and minimum: {nr2}") 
    else:
        print("Beide getallen zijn even groot")
        return str("Beide getallen zijn even groot")