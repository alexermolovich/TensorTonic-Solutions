import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    # recieveing two input vectors of n size 
    """
    Returns the cosine similarity as a Python float.
    """
    modulus_a = math.sqrt(sum(x**2 for x in a))
    modulus_b = math.sqrt(sum(x**2 for x in b))
    output = 0
    for i in range(0, len(a)):
        output += a[i] * b[i]
    return output/max(1, (modulus_a * modulus_b))