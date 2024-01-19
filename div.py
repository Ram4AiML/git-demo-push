def div(a,b):
    """
    Division two numbers.

    Parameters:
    - a (int): The first number.
    - b (int): The second number.

    Returns:
    int: The Division of a and b.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
try:
    result = div(2, 3)
    print("Division of a and b :", result)
except ValueError as e:
    print("Error:", e)

