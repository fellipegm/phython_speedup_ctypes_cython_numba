from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

setup(
    name='Monte Carlo simulation',
    ext_modules=[
        Extension('_dice6_cy', ['plain_cython.pyx'],
            include_dirs=[numpy.get_include()])
        ],
    cmdclass={'build_ext': build_ext},
)