def div(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
try:
    result = div(2, 3)
    print("Division of a and b :", result)
except ValueError as e:
    print("Error:", e)

