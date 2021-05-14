
import numpy as np
cimport numpy as np
np.import_array()


cdef extern from "filter_pure_c.h":
    int fofilter_pure_c(double *input, double *output, double dt, double tau, int n)


def fofilter_pure_c_cython_wrap(np.ndarray[double, ndim=1, mode="c"] input, double dt, double tau):
    if not input.flags['C_CONTIGUOUS']:
        input = np.ascontiguousarray(input)

    cdef np.ndarray[double, ndim=1, mode="c"] output
    output = np.zeros_like(input)
    if not output.flags['C_CONTIGUOUS']:
        output = np.ascontiguousarray(output)

    cdef double[::1] input_memview = input
    cdef double[::1] output_memview = output
    out = fofilter_pure_c(&input_memview[0], &output_memview[0], dt, tau, input_memview.shape[0])

    return output