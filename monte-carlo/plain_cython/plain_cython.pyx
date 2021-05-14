# cython: profile=True

import random
from func_timer import timing_val
import numpy as np
cimport numpy as np
import cython
from libc.stdlib cimport rand, RAND_MAX


# cython -a Gera HTML para verificar quais partes do código ficam em c e outras em python.

@timing_val
def dice6_cy_randpy(int N, int ndice, int nsix):
    cdef int M = 0
    # no of successful events
    cdef int six, r
    cdef double p
    for i in range(N):
        # repeat N experiments
        six = 0
        # how many dice with six eyes?
        for j in range(ndice):
            r = random.randint(1, 6) # roll die no. j
            if r == 6:
                six += 1
            if six >= nsix:
                M += 1
    p = float(M)/N
    return p


@timing_val
@cython.boundscheck(False) # turn off array bounds check
@cython.wraparound(False) # turn off negative indices ([-1,-1])
def dice6_cy_np(int N, int ndice, int nsix):
    # Use numpy to generate all random numbers
    cdef int M = 0
    cdef int six, r # no of successful events
    cdef double p
    cdef np.ndarray[np.int_t, ndim=2, mode='c'] eyes = \
        np.random.random_integers(1, 6, (N, ndice))
    for i in range(N):
        six = 0
        # how many dice with six eyes?
        for j in range(ndice):
            r = eyes[i,j] # roll die no. j
            if r == 6:
                six += 1
            if six >= nsix: # successful event?
                M += 1
    p = float(M)/N
    return p


@timing_val
def dice6_cy_randc(int N, int ndice, int nsix):
    cdef int M = 0
    # no of successful events
    cdef int six, r
    cdef double p
    for i in range(N):
        six = 0 # how many dice with six eyes?
        for j in range(ndice): # Roll die no. j
            r = 1 + int(6.0*rand()/RAND_MAX)
            if r == 6:
                six += 1
            if six >= nsix: # successful event?
                M += 1
    p = float(M)/N
    return p