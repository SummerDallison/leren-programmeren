def determine_biggest(nr1: int, nr2: int) -> str:
    if nr1 < nr2:
        return (f"Maximum: {nr2} and minimum: {nr1}") 
    elif nr1 > nr2:
        return (f"Maximum: {nr1} and minimum: {nr2}")
    else:
        return "Beide getallen zijn even groot"