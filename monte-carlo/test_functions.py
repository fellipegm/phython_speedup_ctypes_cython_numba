from pure_python.pure import dice6_py
from vectorized.mc_vectorized import dice6_vec1
from plain_cython._dice6_cy import dice6_cy_randpy, dice6_cy_np, dice6_cy_randc
from pure_c._dice6_cpure import dice6_cwrap


N = 100000
ndice = 2
nsix = 2

n_tests = 10

funcs = [dice6_py, dice6_vec1, dice6_cy_randpy, dice6_cy_np, dice6_cy_randc, dice6_cwrap]

for func in funcs:
    meanTime = 0
    for _ in range(n_tests):
        p = func(N, ndice, nsix)
        meanTime += p[0]/n_tests
    print(f'CPU time {p[2]}: {meanTime}, probability = {p[1]}')
