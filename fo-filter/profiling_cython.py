import cProfile, pstats
from plain_cython._plain_cython import fofilter_pure_cython_np
import numpy as np

from c_driver import 


n_tests = 1
tau = 0.005
dt = 1e-6
n_cycles = 100.0
f = 1/2/np.pi
N = f/dt*n_cycles

x = np.linspace(0.0, n_cycles*2.0*np.pi, int(N))
y = np.sin(x)
y = y + np.random.normal(0, 0.01, y.shape)

statement = 'fofilter_pure_cython_np(y, dt, tau)'
cProfile.runctx(statement, globals(), locals(), 'tmp_profile.dat')
s = pstats.Stats('tmp_profile.dat')
s.strip_dirs().sort_stats('time').print_stats(30)