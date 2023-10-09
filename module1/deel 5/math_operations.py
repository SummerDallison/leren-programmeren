# example:
def increment(nr: float) -> float:
  return nr + 1

def decrement(nr: float) -> float:
  return nr -1

def add(nr: float) -> float:
  return nr + nr

def substract(nr: float) -> float:
  return nr - nr

def multiply(nr: float) -> float:
  return nr * nr

def divide(nr: float) -> float:
  try:
    result = nr/nr
    return result
  except ZeroDivisionError:
    return None