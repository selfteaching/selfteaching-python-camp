def is_prime(n):
    """
    Return a boolean  value base upon
    whether  the argument n is a prime number.
    """
    if n<2:
        return False
    if n==2:
        return True
    for m in range(2,int(n**0.5)+1):
        if (n%m) == 0:
            return False
        else:
            return True
    
