import numpy as np

def dot_product(x: list, y: list) -> float:
    
    """
    Returns the dot product as a float.
    """
    output = 0
    array_size = len(x) 
  
    for i in range(0, array_size):
        output += x[i] * y[i]    
   
    return float(output) 
    