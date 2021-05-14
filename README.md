# Comparison of Python speed-up with Cython, ctypes and numba 

## First order filter speed-up results:

Results of the first order filter using a sinusoidal input signal with 1000 cycles and 1e-6 sampling time

CPU time fofilter_plain: 106.13 s
CPU time fofilter_pure_cython_np: 1.26 s
CPU time fofilter_pure_c_cython_wrap: 1.01 s
CPU time filter_c_ctypes_wrap: 1.69 s
CPU time fofilter_plain_numba: 2.82 s

## License

AGPL V3

