def isPrime(n):
    """
    Takes n an integer
    Returns True if n is prime 
    else False
    """
    import math
    return all([n%i for i in range(2, int(math.sqrt(n)+1))])