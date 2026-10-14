def add_numbers(a, b):
    return a + b    

def subtract_numbers(a, b):
   return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    """Return a divided by b.
    Raises:
    ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Denominator must not be zero")
    return a / b
