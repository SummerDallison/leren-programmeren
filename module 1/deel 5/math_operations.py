# example:
def increment(nr: float) -> float:
  return nr + 1

def decrement(nr: float) -> float:
  return nr -1

def add(nr1: float, nr2: float) -> float:
  return nr1 + nr2

def substract(nr1: float, nr2: float) -> float:
  return nr1 - nr2

def multiply(nr1: float, nr2: float) -> float:
  return nr1 * nr2

def divide(nr1: float, nr2: float) -> float:
  try:
    result = nr1/nr2
    return result
  except ZeroDivisionError:
    return None