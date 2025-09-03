def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    """
    Return the product of a and b.
    
    Performs a * b and returns the result. Works with numeric types and any objects that implement the __mul__ operator (for example, sequence repetition).
    """
    return a * b

def divide(a, b):
    """
    Return the quotient of a divided by b.
    
    Parameters:
        a: Dividend — a numeric value supporting division.
        b: Divisor — a numeric value; must not be zero.
    
    Returns:
        The result of a / b (numeric).
    
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b
ded f test_add():
    pass