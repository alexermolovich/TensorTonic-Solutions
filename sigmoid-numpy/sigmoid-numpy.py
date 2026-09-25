import numpy as np
import math

def sigmoid(x: list | float) -> np.ndarray | float:
    
    x_arr = np.asarray(x, dtype=float)
    res = 1 / (1 + np.exp(-x_arr))
    return res.item() if np.isscalar(x) else res
