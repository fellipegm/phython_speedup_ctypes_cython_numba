import numpy as np
from numba import njit

@njit
def fofilter_plain_numba(input: np.ndarray, dt: float, tau: float) -> np.ndarray:

    if input.shape[0] == 0:
        return None
        
    output = np.zeros(input.shape[0], dtype=np.float64)

    a = tau / (tau + dt)
    b = dt / (tau + dt)
    for ii in range(1, input.shape[0]):
        output[ii] = input[ii]*b + output[ii-1]*a
    
    return output