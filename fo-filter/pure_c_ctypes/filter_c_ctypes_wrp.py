"""Example of wrapping a C library function that accepts a C double array as
    input using the numpy.ctypeslib. """

import numpy as np
import numpy.ctypeslib as npct
from ctypes import c_int, c_double

# input type for the cos_doubles function
# must be a double array, with single dimension that is contiguous
array_1d_double = npct.ndpointer(dtype=np.double, ndim=1, flags='CONTIGUOUS')

# load the library, using numpy mechanisms
libcd = npct.load_library("lib_fofilter", "./pure_c_ctypes/")

# setup the return types and argument types
libcd.fofilter_pure_c.restype = None
libcd.fofilter_pure_c.argtypes = [array_1d_double, array_1d_double, c_double, c_double, c_int]


def filter_c_ctypes_wrap(in_array, dt, tau):
    out_array = npct.array(in_array, dtype=np.float64)
    libcd.fofilter_pure_c(in_array, out_array, dt, tau, len(in_array))
    return out_array