# SCIFM0004_project_1
Accelerating MCS code using a variety of techniques.
Setup needs to be compiled first by typing:
  python setup_cython.py build_ext -fi -lm
  
-lm flag included to call functions from math library

Cythonized version of the code needs to be called using the run file:

python cython_run.py 50 50 0.5 0 
