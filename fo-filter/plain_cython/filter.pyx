

from func_timer import timing_val
import numpy as np
cimport numpy as np
cimport cython


@cython.boundscheck(False) # turn off array bounds check
@cython.wraparound(False) # turn off negative indices ([-1,-1])
def fofilter_pure_cython_np(np.ndarray[np.float64_t, ndim=1] input, float dt, float tau):
    cdef np.ndarray[np.float64_t, ndim=1] output = np.zeros(input.shape[0], dtype=np.float64)

    cdef double a = tau / (tau + dt)
    cdef double b = dt / (tau + dt)

    cdef int i

    for i in range(1, len(input)):
        output[i] = input[i]*b + output[i-1]*a
    
    return output
