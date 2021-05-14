import cProfile, pstats
from plain_cython._dice6_cy import dice6_cy1

N = 100000
ndice = 2
nsix = 2
statement = 'dice6_cy1(N, ndice, nsix)'
cProfile.runctx(statement, globals(), locals(), 'tmp_profile.dat')
s = pstats.Stats('tmp_profile.dat')
s.strip_dirs().sort_stats('time').print_stats(30)