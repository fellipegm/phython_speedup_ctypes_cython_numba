from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy


sources = ['filter_wrap.pyx', 'filter_pure_c.c']

setup(
    name='First Order Filter Pure C',
    ext_modules=[Extension('_fofilter_pure_c', sources, include_dirs=[numpy.get_include()])],
    cmdclass={'build_ext': build_ext},
)