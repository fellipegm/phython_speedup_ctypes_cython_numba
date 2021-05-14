#%%
import os
print(os.getcwd())

# %%
import time
import numpy as np
from pure_python.plain import fofilter_plain
from plain_cython._plain_cython import fofilter_pure_cython_np
from pure_c_cython._fofilter_pure_c import fofilter_pure_c_cython_wrap
from pure_c_ctypes import filter_c_ctypes_wrp as filter_ctypes_wrap
from filter_numba.plain_numba import fofilter_plain_numba
import matplotlib.pylab as plt
# %%
n_tests = 1
tau = 0.005
dt = 1e-6
n_cycles = 1000.0
f = 1/2/np.pi
N = f/dt*n_cycles

x = np.linspace(0.0, n_cycles*2.0*np.pi, int(N))
y = np.sin(x)
y = y + np.random.normal(0, 0.01, y.shape)
y = np.ascontiguousarray(y)

funcs = [
            fofilter_plain, 
            fofilter_pure_cython_np, 
            fofilter_pure_c_cython_wrap, 
            filter_ctypes_wrap.filter_c_ctypes_wrap, 
            fofilter_plain_numba
        ]

# %%
results = []
s_write = ''
for func in funcs:
    meanTime = 0
    for _ in range(n_tests):
        t1 = time.time()
        res = func(y, dt, tau)    
        t2 = time.time()
        meanTime += (t2-t1)/n_tests
        results.append(res)
    s_write += f'CPU time {func.__name__}: {meanTime}\n'

print(s_write)
with open('dados.txt', 'w') as f:
    f.write(s_write)


# %%
# names = [func.__name__ for func in funcs]
# plain_python = np.array(results[0], dtype=np.float64)
# for result, name in zip(results[1:], names[1:]):
#     plt.plot(x, plain_python)
#     plt.plot(x, result)
#     plt.legend([names[0], name])
#     plt.show()


# for ii, func in enumerate(funcs[1:]):
#     # print(f'func: {func.__name__} zero: {results[ii][0]}')
#     max_error = np.max(np.abs( plain_python - results[ii] ))
#     print(f'Max error {func.__name__}: {max_error}')


# %%
