from math import sqrt, ceil

# (Kristian) My favorite function: 
# The sieve of eratosthenes
def sieve_of_eratosthenes(n: int) -> set:
    """ Find all prime numbers less than n.
    """
    numberline = set(range(2, n))

    for p in range(2, ceil(sqrt(n)) ):
        for num in range(2*p, n, p):
            numberline.discard(num)
            
    return numberline

# Helges favorite function:
def add_test(x,y):
    """Add two numbers"""
    new_number = x + y
    return new_number
