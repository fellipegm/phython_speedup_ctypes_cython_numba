from func_timer import timing_val

cdef extern from "monte_carlo.h":
    double dice6(int N, int ndice, int nsix)

@timing_val
def dice6_cwrap(int N, int ndice, int nsix):
    return dice6(N, ndice, nsix)