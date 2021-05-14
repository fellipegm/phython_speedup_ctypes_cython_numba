import numpy as np


def fofilter_plain(input: np.ndarray, dt: float, tau: float) -> list:

    if input.shape[0] == 0:
        return None
        
    output = np.zeros(input.shape[0], dtype=np.float64)
    output[0] = 0.0

    a = tau / (tau + dt)
    b = dt / (tau + dt)
    for i in range(1, len(input)):
        output[i] = input[i]*b + output[i-1]*a
    
    return output