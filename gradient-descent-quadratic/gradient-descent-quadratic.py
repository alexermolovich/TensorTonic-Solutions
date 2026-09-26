def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    
    x = x0
    
    for _ in range(steps):
        df_dx = 2 * a * x + b
        
        x = x - lr * df_dx
        
    return x