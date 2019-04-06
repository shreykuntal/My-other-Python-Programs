def PPrime(n):
    """
    Takes n an integer
    Returns a list of prime numbers between 1 and n
    """
    import math
    return [x for x in range(2, n) if all([x%i for i in range(2, int(math.sqrt(x)+1))])]
print(PPrime(99999))