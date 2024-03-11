from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(name="cython_leb_lash",
      ext_modules=cythonize("cython_leb_lash.pyx", compiler_directives={'language_level' : "3"}),
      include_dirs=[numpy.get_include()])
