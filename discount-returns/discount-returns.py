def discount_returns(rewards: list, gamma: float) -> list:
    """
    Returns the discounted return at every timestep.
    """
    returns = [0.0] * len(rewards)
    running_return = 0.0 # Basically, running return is accumulation starting at the end of the list 
    
    for i in range(len(rewards) - 1, -1, -1):
        # This is the main formula that:
        # 1. rewrads[i] = r[t]
        # 2. Gamma is Y
        # 3. running_return - is the G_t+1
        running_return = float(rewards[i]) + gamma * running_return 
        returns[i] = running_return

    return returns