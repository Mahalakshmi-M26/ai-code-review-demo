def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)
print(result)

def subtract_numbers(a, b):
    return a - b    

subtract_result = subtract_numbers(10, 5)
print(subtract_result)

def multiply_numbers(a, b):
    return a * b

multiply_result = multiply_numbers(5, 10)
print(multiply_result)

def divide_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
