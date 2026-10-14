import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    m = len(A)     
    n = len(A[0])  
    
    output = np.zeros((n, m))
   
    for j in range(m):
   
        for k in range(n):
       
            output[k, j] = A[j][k]

    return output