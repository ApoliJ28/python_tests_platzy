def sum(a, b):
    """ 
    >>> sum(5,7)
    12
    
    >>> sum(4,-4)
    0
    """
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    """ 
    >>> divide(10,0)
    Traceback (most recent call last):
    ZeroDivisionError: No se puede dividir por cero.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return a /b