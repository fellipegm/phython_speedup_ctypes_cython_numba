from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


sources = ['pure_c_wrap.pyx', 'monte_carlo.c']
setup(
    name='Monte Carlo simulation',
    ext_modules=[Extension('_dice6_cpure', sources)],
    cmdclass={'build_ext': build_ext},
)