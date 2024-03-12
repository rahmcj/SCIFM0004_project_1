# SCIFM0004_project_1
Accelerating MCS code using a variety of techniques.
For all versions apart from cython please compile using the following text:
python LebwholLasher.py 50 50 0.5 0


Instructions for cythonised data:
needs to be compiled first by typing:
  python setup_cython.py build_ext -fi -lm
  
-lm flag included to call functions from math library

Cythonized version of the code needs to be called using the run file:
python cython_run.py 50 50 0.5 0 
