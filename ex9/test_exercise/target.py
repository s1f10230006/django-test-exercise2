import math

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def permutation(n, k):
    if n <= 0:
        return 0
    if k < 0:
        return 0
    if n < k:
        return 0
    
    result = 1
    for i in range(k):
        result *= (n - i)
    return result