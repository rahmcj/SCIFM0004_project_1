from distutils.core import setup
from Cython.Build import cythonize

setup(name="cython_leb_lash",
      ext_modules=cythonize("cython_leb_lash.pyx"))